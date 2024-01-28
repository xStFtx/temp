import numpy as np

class FourierSeries:
    def __init__(self, P, N):
        self.P = P  # Period of the function
        self.N = N  # Number of terms in the series

    def compute_cn(self, n):
        # Compute the Fourier coefficients for a square wave.
        if n % 2 == 0:
            return 0
        else:
            return 1 / (1j * np.pi * n)

    def series_approximation(self, x):
        # Compute the Fourier series approximation for the value x.
        f_approx = np.zeros_like(x, dtype=complex)
        for n in range(-self.N, self.N + 1):
            c_n = self.compute_cn(n)
            f_approx += c_n * np.exp(1j * 2 * np.pi * n * x / self.P)
        return f_approx.real

# Example usage:
P = 2 * np.pi  # Period of the square wave
N = 10  # Number of terms in the series
fourier = FourierSeries(P, N)

# Compute the series approximation for a range of x values
x_values = np.linspace(-P / 2, P / 2, 1000)
f_approx = fourier.series_approximation(x_values)

# You can plot the result using matplotlib if you wish
import matplotlib.pyplot as plt

plt.plot(x_values, f_approx)
plt.title('Fourier Series Approximation of a Square Wave')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
