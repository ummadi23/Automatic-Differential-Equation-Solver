
import sympy as sp
from solver.graph_plotter import plot_solution

t = sp.symbols('t', positive=True)

solution = 7*sp.exp(-2*t) - 5*sp.exp(-3*t)

plot_solution(solution)
