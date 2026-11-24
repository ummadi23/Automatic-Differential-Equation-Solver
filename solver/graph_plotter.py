 
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def plot_solution(solution, save_path=None):

    t = sp.symbols('t', positive=True)

    function = sp.lambdify(t, solution, modules='numpy')

    time = np.linspace(0, 10, 200)

    values = function(time)

    plt.figure(figsize=(8, 5))

    plt.plot(time, values, label='y(t)')

    plt.title("Differential Equation Solution")
    plt.xlabel("Time (t)")
    plt.ylabel("y(t)")
    plt.grid(True)
    plt.legend()

    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()
