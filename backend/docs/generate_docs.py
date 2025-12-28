from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import os

# Folder where PDFs will be saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------
# PDF 1: Testing Evidence
# ---------------------
test_pdf_path = os.path.join(BASE_DIR, "Testing_Evidence_ToDo_Rakhi.pdf")
styles = getSampleStyleSheet()
doc = SimpleDocTemplate(test_pdf_path, pagesize=A4)
story = []

story.append(Paragraph("<b>Testing Evidence - To-Do List App</b>", styles['Title']))
story.append(Spacer(1, 0.3 * inch))

info = [
    "Developer: Rakhi Agarwal",
    "Email: rakhi.ag.26@gmail.com",
    "Phone: 9870612158",
    "LinkedIn: linkedin.com/in/rakhi-agarwal-ab07881a5",
    "Submission Date: 30 Dec 2025"
]
for line in info:
    story.append(Paragraph(line, styles['Normal']))
story.append(PageBreak())

story.append(Paragraph("<b>Test Cases Executed</b>", styles['Heading2']))
tests = [
    "Task List UI — PASS",
    "Add Task UI — PASS",
    "Update Task UI — PASS",
    "Delete Task UI — PASS",
    "API JSON /api/tasks — PASS",
    "Automation (pytest) — PASS",
]
for t in tests:
    story.append(Paragraph(f"✔ {t}", styles['Normal']))
story.append(Spacer(1, 0.3 * inch))

story.append(Paragraph("<b>Conclusion:</b> All core features validated successfully.", styles['Heading3']))
story.append(Paragraph("GitHub: github.com/RakhiAg158/Python_PELOCAL_ProjectWithAPIsAndTemplates", styles['Normal']))

doc.build(story)

# ---------------------
# PDF 2: Submission Report
# ---------------------
report_pdf_path = os.path.join(BASE_DIR, "Submission_Report_ToDo_Rakhi.pdf")
doc = SimpleDocTemplate(report_pdf_path, pagesize=A4)
story = []

story.append(Paragraph("<b>Submission Report</b>", styles['Title']))
story.append(Spacer(1, 0.3 * inch))
for line in info:
    story.append(Paragraph(line, styles['Normal']))
story.append(PageBreak())

story.append(Paragraph("<b>Project Objective</b>", styles['Heading2']))
story.append(Paragraph(
    "Develop a To-Do List Web App using Django with Raw SQL, REST APIs, Docker support and testing.",
    styles['Normal']
))
story.append(PageBreak())

story.append(Paragraph("<b>Requirements Implemented</b>", styles['Heading2']))
for req in [
    "CRUD Tasks",
    "REST APIs",
    "SQLite + Raw SQL",
    "Template based UI",
    "Docker Deployment",
    "Automated Testing"
]:
    story.append(Paragraph(f"✔ {req}", styles['Normal']))
story.append(PageBreak())

story.append(Paragraph("<b>Architecture</b>", styles['Heading2']))
story.append(Paragraph(
    "UI → Views → Service Layer → Raw SQL → Database",
    styles['Heading4']
))
story.append(Paragraph("Clean separation of layers for easy maintainability.", styles['Normal']))
story.append(PageBreak())

story.append(Paragraph("<b>API Documentation</b>", styles['Heading2']))
apis = [
    "GET /api/tasks/",
    "POST /api/tasks/",
    "GET /api/tasks/<id>/",
    "PUT /api/tasks/<id>/",
    "DELETE /api/tasks/<id>/"
]
for a in apis:
    story.append(Paragraph(f"✔ {a}", styles['Normal']))
story.append(PageBreak())

story.append(Paragraph("<b>Testing Summary</b>", styles['Heading2']))
for t in tests:
    story.append(Paragraph(f"✔ {t}", styles['Normal']))
story.append(PageBreak())

story.append(Paragraph("<b>Conclusion</b>", styles['Heading2']))
story.append(Paragraph(
    "Backend fully functional and ready for demonstration.",
    styles['Normal']
))

doc.build(story)

print("🎉 PDFs generated successfully in docs folder!")
