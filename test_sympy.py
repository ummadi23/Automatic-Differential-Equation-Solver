
import sympy as sp

# Define mathematical variables
t, s = sp.symbols('t s', positive=True)

# Define a function
f = sp.exp(-2*t)

# Calculate Laplace Transform
F = sp.laplace_transform(f, t, s, noconds=True)

print("Original Function:", f)
print("Laplace Transform:", F)

# Calculate Inverse Laplace Transform
result = sp.inverse_laplace_transform(F, s, t)

print("Inverse Laplace Transform:", result)
