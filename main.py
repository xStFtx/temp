import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from functools import lru_cache
from multiprocessing import Pool

class AdvancedFourierSeries:
    def __init__(self, f, P, N):
        self.f = f
        self.P = P
        self.N = N

    @lru_cache(maxsize=None)
    def compute_coefficients(self):
        # Parallel computation of coefficients
        with Pool() as pool:
            coefficients = pool.map(self.integrate_coefficient, range(-self.N, self.N + 1))
        return coefficients

    def integrate_coefficient(self, n):
        # Integral calculation for a single coefficient
        cn, _ = quad(lambda x: self.f(x) * np.exp(-1j * 2 * np.pi * n * x / self.P), -self.P/2, self.P/2)
        return (1 / self.P) * cn

    def series_approximation(self, x):
        coefficients = self.compute_coefficients()
        n_values = np.arange(-self.N, self.N + 1)
        exp_values = np.exp(1j * 2 * np.pi * np.outer(n_values, x) / self.P)
        return np.dot(coefficients, exp_values).real

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
