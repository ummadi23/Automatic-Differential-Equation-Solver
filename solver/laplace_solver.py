
import sympy as sp

# Define symbols and function
t, s = sp.symbols('t s')
y = sp.Function('y')

# Define the differential equation
equation = sp.Eq(sp.diff(y(t), t) + 2*y(t), 0)

# Initial condition
initial_condition = {y(0): 1}

# Apply Laplace Transform
Y = sp.symbols('Y')

laplace_eq = (
    s*Y - initial_condition[y(0)] + 2*Y
)

print("Laplace Transform Equation:")
print(laplace_eq, "= 0")

# Solve for Y(s)
Y_solution = sp.solve(laplace_eq, Y)[0]

print("\nY(s) =", Y_solution)

# Apply Inverse Laplace Transform
final_solution = sp.inverse_laplace_transform(
    Y_solution, s, t
)

print("\nFinal Solution:")
print("y(t) =", final_solution)
