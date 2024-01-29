import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from functools import lru_cache

class AdvancedFourierSeries:
    def __init__(self, f, P, N):
        self.f = f  # The periodic function
        self.P = P  # Period of the function
        self.N = N  # Number of terms in the series

    @lru_cache(maxsize=None)
    def compute_coefficients(self):
        # Efficiently compute the Fourier coefficients using quad (adaptive quadrature)
        coefficients = []
        for n in range(-self.N, self.N + 1):
            cn, _ = quad(lambda x: self.f(x) * np.exp(-1j * 2 * np.pi * n * x / self.P), -self.P/2, self.P/2)
            cn = (1 / self.P) * cn
            coefficients.append(cn)
        return coefficients

    def series_approximation(self, x):
        # Compute the Fourier series approximation for the value x
        coefficients = self.compute_coefficients()
        f_approx = np.zeros_like(x, dtype=complex)
        for n, cn in enumerate(coefficients):
            n_shifted = n - self.N  # Shift index to go from -N to N
            f_approx += cn * np.exp(1j * 2 * np.pi * n_shifted * x / self.P)
        return f_approx.real

    def plot_approximation(self):
        x_values = np.linspace(-self.P / 2, self.P / 2, 1000)
        f_approx = self.series_approximation(x_values)

        plt.plot(x_values, f_approx)
        plt.title('Advanced Fourier Series Approximation')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.show()

# Example usage
P = 2 * np.pi
N = 50
f = np.vectorize(lambda x: 1 if x < 0 else -1)

advanced_fourier = AdvancedFourierSeries(f, P, N)
advanced_fourier.plot_approximation()
