 
from flask import Flask, render_template, request, send_file
import sympy as sp
import os

from solver.second_order_solver import solve_second_order
from solver.graph_plotter import plot_solution
from solver.pdf_generator import generate_pdf

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/solver", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":
        try:
            a = sp.Rational(request.form["a"])
            b = sp.Rational(request.form["b"])
            y0 = sp.Rational(request.form["y0"])
            v0 = sp.Rational(request.form["v0"])

            equation, Y, answer, partial_fractions = solve_second_order(
                 a, b, y0, v0
            )

            graph_path = os.path.join(
                app.static_folder, "solution.png"
            )

            plot_solution(answer, graph_path)

            result = {
                "a": a,
                "b": b,
                "y0": y0,
                "v0": v0,
                "equation": equation,
                "Y": Y,
                "answer": answer,
                "partial_fractions": partial_fractions
            }
            app.config["solution_result"] = result

        except (ValueError, TypeError, ZeroDivisionError,
                sp.SympifyError):
            error = "Please enter valid numerical values."

     
    if result:
       return render_template("results.html", result=result)

    return render_template(
      "solver.html",
      result=None,
      error=error
)
@app.route("/download-pdf")
def download_pdf():

    result = app.config.get("solution_result")

    if not result:
        return "Please solve the equation first."

    graph_path = os.path.join(
        app.static_folder, "solution.png"
    )

    pdf_path = os.path.join(
        app.root_path, "solution.pdf"
    )

    generate_pdf(result, graph_path, pdf_path)

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name="Differential_Equation_Solution.pdf"
    )
if __name__ == "__main__":
    app.run(debug=True)
