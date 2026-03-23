import numpy as np
import matplotlib.pyplot as plt

num_symbols = 1000

x_int = np.random.randint(0, 4, num_symbols)
x_degrees = x_int * 360 / 4 + 45
x_radians = x_degrees * np.pi / 180.0
x_symbols = np.cos(x_radians) + 1j * np.sin(x_radians)

plt.figure()
plt.plot(np.real(x_symbols), np.imag(x_symbols), '.')
plt.grid(True)

n = (np.random.randn(num_symbols) + 1j * np.random.randn(num_symbols)) / np.sqrt(2)
noise_power = 0.01
phase_noise = np.random.randn(len(x_symbols)) * 0.3
r = (x_symbols * np.exp(1j * phase_noise)) + n * np.sqrt(noise_power)

plt.figure()
plt.plot(np.real(r), np.imag(r), '.')
plt.grid(True)
plt.show()
