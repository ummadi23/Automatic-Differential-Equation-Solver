
from dynamic_solver import solve_equation

def explain_solution():

    print("\nAUTOMATIC DIFFERENTIAL EQUATION SOLVER")
    print("--------------------------------------")

    # Get input from user
    a = input("Enter the coefficient a: ")
    y0 = input("Enter initial condition y(0): ")

    try:
        a, y0, laplace_eq, Y_solution, final_answer = (
            solve_equation(a, y0)
        )

        print("\nSTEP-BY-STEP EXPLANATION")
        print("------------------------")

        # Step 1
        print("\nStep 1: Given Differential Equation")
        print(f"y' + ({a})y = 0")
        print(f"Initial condition: y(0) = {y0}")

        # Step 2
        print("\nStep 2: Apply Laplace Transform")
        print("Formula: L{y'} = sY(s) - y(0)")
        print("Transformed equation:")
        print(spacing(laplace_eq))

        # Step 3
        print("\nStep 3: Solve for Y(s)")
        print("Y(s) =", Y_solution)

        # Step 4
        print("\nStep 4: Apply Inverse Laplace Transform")
        print("Final solution:", final_answer)

        # Step 5
        print("\nStep 5: Final Answer")
        print("y(t) =", final_answer)

    except (ValueError, TypeError, ZeroDivisionError):
        print("\nInvalid input. Please enter valid rational numbers.")

def spacing(expression):
    return str(expression) + " = 0"

if __name__ == "__main__":
    import sympy as sp
    explain_solution()
