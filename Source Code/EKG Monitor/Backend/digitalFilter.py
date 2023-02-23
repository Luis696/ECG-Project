import scipy
from scipy import signal
import numpy as np
from collections import deque  # import queue for LiveFilter
import matplotlib.pyplot as plt


class LiveFilter:
    """Base class for live filters.
    """
    def process(self, x):
        # do not process NaNs
        if np.isnan(x):
            return x

        return self._process(x)

    def __call__(self, x):
        return self.process(x)

    def _process(self, x):
        raise NotImplementedError("Derived class must implement _process")


class LiveLFilter(LiveFilter):
    def __init__(self, b, a):
        """Initialize live filter based on difference equation.

        Args:
            b (array-like): numerator coefficients obtained from scipy.
            a (array-like): denominator coefficients obtained from scipy.
        """
        self.b = b
        self.a = a
        self._xs = deque([0] * len(b), maxlen=len(b))
        self._ys = deque([0] * (len(a) - 1), maxlen=len(a)-1)

    def _process(self, x):
        """Filter incoming data with standard difference equations.
        """
        self._xs.appendleft(x)  # Note that by appending values from the left, the coefficients b_k and a_k are properly aligned with the past inputs $x[n-k]$ and outputs $y[n-k]$
        y = np.dot(self.b, self._xs) - np.dot(self.a[1:], self._ys)  # dot product between signal and filter coefficients
        y = y / self.a[0]
        self._ys.appendleft(y)

        return y


np.random.seed(42)  # for reproducibility
# create time steps and corresponding sine wave with Gaussian noise
fs = 30  # sampling rate, Hz
ts = np.arange(0, 5, 1.0 / fs)  # time vector - 5 seconds

ys = np.sin(2*np.pi * 1.0 * ts)  # signal @ 1.0 Hz, without noise
yerr = 0.5 * np.random.normal(size=len(ts))  # Gaussian noise
yraw = ys + yerr

# Butterworth low-pass filter with frequency cutoff at 2.5 Hz
b, a = scipy.signal.iirfilter(4, Wn=2.5, fs=30, btype="low", ftype="butter")
live_lfilter = LiveLFilter(b, a)
# simulate live filter - passing values one by one
y_live_lfilter = [live_lfilter(y) for y in yraw]


plt.figure(figsize=[6.4, 2.4])
plt.plot(ts, yraw, label="Noisy signal")
plt.plot(ts, y_live_lfilter, lw=4, ls="dashed", label="LiveLFilter")
plt.legend(loc="lower center", bbox_to_anchor=[0.5, 1], ncol=3, fontsize="smaller")
plt.xlabel("Time / s")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()

