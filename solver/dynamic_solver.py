
import sympy as sp

def solve_equation(a_value, initial_value):

    # Define mathematical symbols
    t, s = sp.symbols('t s', positive=True)
    Y = sp.symbols('Y')

    # Convert user inputs into mathematical numbers
    a = sp.Rational(a_value)
    y0 = sp.Rational(initial_value)

    # Apply Laplace Transform
    laplace_equation = (s + a) * Y - y0

    # Solve for Y(s)
    Y_solution = sp.solve(laplace_equation, Y)[0]

    # Apply inverse Laplace Transform
    result = sp.inverse_laplace_transform(
        Y_solution, s, t
    )

    # Simplify for positive time
    final_answer = sp.simplify(
        result.subs(sp.Heaviside(t), 1)
    )

    return a, y0, laplace_equation, Y_solution, final_answer
