import numpy as np
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)
    if N == 1:
        return x
    twiddle_factors = np.exp(-2j * np.pi * np.arange(N//2) / N)
    x_even = fft(x[::2])
    x_odd = fft(x[1::2])
    return np.concatenate([x_even + twiddle_factors * x_odd,
                           x_even - twiddle_factors * x_odd])


Fs = 1e6 # Hz
f_offset = 0.2e6 # Hz 
N = 1024 # Number of samples and FFT size

t = np.arange(N) / Fs
s = np.exp(2j * np.pi * f_offset * t)
s = s * np.hamming(N)
n = (np.random.randn(N) + 1j * np.random.randn(N)) / np.sqrt(2)
r = s + n

X = fft(r)
X_shifted = np.roll(X, N//2)
X_mag = 10 * np.log10(np.abs(X_shifted)**2)

f = np.linspace(Fs / -2, Fs / 2, N) / Fs
plt.figure(0)
plt.plot(f, X_mag)
plt.plot(f[np.argmax(X_mag)], np.max(X_mag), 'rx')
plt.grid()
plt.xlabel('Frequency [MHz]')
plt.ylabel('Magnitude [dB]')
plt.show()
