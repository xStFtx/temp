import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import multiprocessing
import os

class AdvancedFourierSeries:
    def __init__(self, f, P, N):
        self.f = f
        self.P = P
        self.N = N

    def compute_coefficients(self):
        # Vectorized computation of coefficients
        n_values = np.arange(-self.N, self.N + 1)
        coefficients = np.array([self.integrate_coefficient(n) for n in n_values])
        return coefficients

    def integrate_coefficient(self, n):
        # Integral calculation for a single coefficient
        cn, error = quad(lambda x: self.f(x) * np.exp(-1j * 2 * np.pi * n * x / self.P), -self.P/2, self.P/2)
        if error > 1e-6:  # Arbitrary error threshold
            print(f"Warning: High integration error for n={n}")
        return (1 / self.P) * cn

    def series_approximation(self, x):
        coefficients = self.compute_coefficients()
        n_values = np.arange(-self.N, self.N + 1)
        exp_values = np.exp(1j * 2 * np.pi * np.outer(n_values, x) / self.P)
        return np.dot(coefficients, exp_values).real

def plot_approximation(advanced_fourier, f):
    x_values = np.linspace(-advanced_fourier.P / 2, advanced_fourier.P / 2, 1000)
    f_approx = advanced_fourier.series_approximation(x_values)
    f_actual = np.vectorize(f)(x_values)

    plt.plot(x_values, f_approx, label='Fourier Approximation')
    plt.plot(x_values, f_actual, label='Actual Function', linestyle='--')
    plt.title('Advanced Fourier Series Approximation')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
P = 2 * np.pi
N = 50
f = lambda x: 1 if x < 0 else -1

advanced_fourier = AdvancedFourierSeries(f, P, N)
plot_approximation(advanced_fourier, f)
