
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer,
    Preformatted, Image
)


def generate_pdf(result, graph_path, pdf_path):

    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph(
        "Automatic Differential Equation Solver",
        styles["Title"]
    ))

    content.append(Spacer(1, 20))

    content.append(Paragraph("Input Values", styles["Heading2"]))

    for key in ["a", "b", "y0", "v0"]:
        content.append(Paragraph(
            f"{key} = {result[key]}",
            styles["Normal"]
        ))

    content.append(Spacer(1, 15))

    sections = [
        ("Laplace Transform", result["equation"]),
        ("Y(s)", result["Y"]),
        ("Partial Fractions", result["partial_fractions"]),
        ("Final Solution", result["answer"])
    ]

    for heading, value in sections:
        content.append(Paragraph(heading, styles["Heading2"]))
        content.append(Preformatted(str(value), styles["Code"]))
        content.append(Spacer(1, 10))

    if os.path.exists(graph_path):
        content.append(Paragraph("Solution Graph", styles["Heading2"]))
        content.append(Image(graph_path, width=400, height=250))

    doc.build(content)
