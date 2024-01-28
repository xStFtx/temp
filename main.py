import numpy as np

class FourierSeries:
    def __init__(self, f, P, N):
        self.f = f  # The periodic function
        self.P = P  # Period of the function
        self.N = N  # Number of terms in the series
        self.coefficients = self.compute_coefficients()  # Pre-compute coefficients

    def compute_coefficients(self):
        # Numerically compute the Fourier coefficients
        coefficients = []
        for n in range(-self.N, self.N + 1):
            integral = self.trapezoidal_rule(lambda x: self.f(x) * np.exp(-1j * 2 * np.pi * n * x / self.P), -self.P/2, self.P/2, 1000)
            cn = (1 / self.P) * integral
            coefficients.append(cn)
        return coefficients

    def trapezoidal_rule(self, func, a, b, N):
        # Compute the integral of a function using the trapezoidal rule
        x = np.linspace(a, b, N + 1)
        y = func(x)
        y_right = y[1:]  # Right endpoints
        y_left = y[:-1]  # Left endpoints
        dx = (b - a) / N
        T = (dx / 2) * np.sum(y_right + y_left)
        return T

    def series_approximation(self, x):
        # Compute the Fourier series approximation for the value x
        f_approx = np.zeros_like(x, dtype=complex)
        for n, cn in enumerate(self.coefficients):
            n_shifted = n - self.N  # Shift index to go from -N to N
            f_approx += cn * np.exp(1j * 2 * np.pi * n_shifted * x / self.P)
        return f_approx.real

# Example usage:
P = 2 * np.pi  # Period of the square wave
N = 50  # Number of terms in the series
f = np.vectorize(lambda x: 1 if x < 0 else -1)  # Square wave function

fourier = FourierSeries(f, P, N)

# Compute the series approximation for a range of x values
x_values = np.linspace(-P / 2, P / 2, 1000)
f_approx = fourier.series_approximation(x_values)

# Plotting the result using matplotlib
import matplotlib.pyplot as plt

plt.plot(x_values, f_approx)
plt.title('Fourier Series Approximation of a Square Wave')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
