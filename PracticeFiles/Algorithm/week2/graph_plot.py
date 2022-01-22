import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    n = np.linspace(1, 10)

    plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
    plt.plot(n, 7*n*n, label="7n^2")
    plt.legend(loc='upper left')
    plt.show()

    n = np.linspace(1, 100)
    plt.plot(n, (7 * n * n + 6 * n + 5)/(7 * n * n), label="7n^2+6n+5")
    plt.show()
