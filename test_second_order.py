
from solver.second_order_solver import solve_second_order

equation, Y, answer = solve_second_order(3, 2, 1, 0)

print("Laplace Equation:")
print(equation, "= 0")

print("\nY(s):")
print(Y)

print("\nFinal Solution:")
print("y(t) =", answer)
