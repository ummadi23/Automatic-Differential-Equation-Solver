
import sympy as sp

def solve_second_order(a_value, b_value, y0_value, v0_value):

    # Define symbols
    t, s = sp.symbols('t s', positive=True)
    Y = sp.symbols('Y')

    # Convert inputs
    a = sp.Rational(a_value)
    b = sp.Rational(b_value)
    y0 = sp.Rational(y0_value)
    v0 = sp.Rational(v0_value)

    # Apply Laplace Transform
    equation = (
        s**2 * Y - s * y0 - v0
        + a * (s * Y - y0)
        + b * Y
    )

    # Solve for Y(s)
    Y_solution = sp.solve(equation, Y)[0]

    # Apply inverse Laplace Transform
    result = sp.inverse_laplace_transform(
        Y_solution, s, t
    )

    # Simplify for positive time
    final_answer = sp.expand(
    sp.simplify(result.subs(sp.Heaviside(t), 1))
)
        # Step-by-step mathematical calculations

    simplified = sp.expand(
        (s**2 + a*s + b) * Y
    )

    numerator = sp.fraction(Y_solution)[0]
    denominator = sp.factor(sp.fraction(Y_solution)[1])

    partial_fractions = sp.apart(Y_solution, s)
    return equation, Y_solution, final_answer, partial_fractions
