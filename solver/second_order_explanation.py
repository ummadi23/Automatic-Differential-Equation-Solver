
import sympy as sp
from second_order_solver import solve_second_order
from graph_plotter import plot_solution

def explain_solution():

    print("\nAUTOMATIC DIFFERENTIAL EQUATION SOLVER")
    print("--------------------------------------")

    # Get input from user
    a = input("Enter coefficient a: ")
    b = input("Enter coefficient b: ")
    y0 = input("Enter initial condition y(0): ")
    v0 = input("Enter initial condition y'(0): ")

    try:
        a, b, y0, v0 = map(
            sp.Rational, [a, b, y0, v0]
        )

        equation, Y_solution, answer = solve_second_order(
            a, b, y0, v0
        )

        s = sp.symbols('s', positive=True)

        print("\nSTEP-BY-STEP EXPLANATION")
        print("------------------------")

        # Step 1
        print("\nStep 1: Given Differential Equation")
        print(f"y'' + ({a})y' + ({b})y = 0")
        print(f"y(0) = {y0}")
        print(f"y'(0) = {v0}")

        # Step 2
        print("\nStep 2: Apply Laplace Transform")
        print("L{y''} = s^2 Y(s) - s*y(0) - y'(0)")
        print("L{y'} = s Y(s) - y(0)")
        print("L{y} = Y(s)")

        # Step 3
        print("\nStep 3: Substitute Initial Conditions")
        print("Laplace equation:")
        print(sp.pretty(equation) + " = 0")

        # Step 4
        print("\nStep 4: Solve for Y(s)")
        print("Y(s) =", sp.factor(Y_solution))

        
        # Step 5
        print("\nStep 5: Apply Partial Fractions")
        partial = sp.apart(Y_solution, s)
        print("Y(s) =", partial)


        

        
        
        # Step 6
        print("\nStep 6: Apply Inverse Laplace Transform")

        print("Using the formula:")
        print("L^-1 {1/(s+a)} = exp(-a*t)")

        print("\nFrom partial fractions:")
        print("Y(s) =", partial)

        # Separate and transform individual terms
        terms = sp.Add.make_args(partial)
        t = sp.symbols('t', positive=True)

        print("\nTransforming each term:")

        for term in terms:
            coefficient, fraction = term.as_coeff_Mul()
            inverse_term = sp.inverse_laplace_transform(
                fraction, s, t
            )
            inverse_term = inverse_term.subs(
                sp.Heaviside(t), 1
            )

            print(
                f"{coefficient} * L^-1({fraction})"
                f" = {sp.simplify(coefficient * inverse_term)}"
            )

        # Calculate complete inverse Laplace answer
        inverse_answer = sp.inverse_laplace_transform(
            partial, s, t
        )

        inverse_answer = sp.expand(
            sp.simplify(
                inverse_answer.subs(sp.Heaviside(t), 1)
            )
        )

        print("\nFinal result after inverse Laplace:")
        print("y(t) =", inverse_answer)


        # Step 7
        print("\nStep 7: Final Answer")
        print("y(t) =", answer)
        print("\nDisplaying Solution Graph...")
        plot_solution(answer) 

    except (ValueError, TypeError, ZeroDivisionError,
            sp.SympifyError):
        print("\nInvalid input. Please enter valid numbers.")

if __name__ == "__main__":
    explain_solution()
