#!/usr/bin/env python3
"""
Create stub PDF documents for testing the reference management system
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
REFERENCES_DIR = REPO_ROOT / "docs" / "references"


def create_stub_pdf(filename: str, title: str, content: str, output_dir: Path):
    """Create a simple stub PDF document"""
    output_path = output_dir / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Create PDF
    c = canvas.Canvas(str(output_path), pagesize=A4)
    width, height = A4

    # Add title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 100, title)

    # Add "STUB DOCUMENT" watermark
    c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(0.8, 0.8, 0.8)
    c.drawString(50, height - 130, "STUB DOCUMENT FOR TESTING")

    # Add content
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica", 12)

    y_position = height - 180
    for line in content.split("\n"):
        if y_position < 50:
            c.showPage()
            y_position = height - 50
            c.setFont("Helvetica", 12)
        c.drawString(50, y_position, line)
        y_position -= 20

    c.save()
    print(f"Created: {output_path.relative_to(REPO_ROOT)}")


def main():
    """Create stub PDFs for testing"""
    print("Creating stub PDF documents for testing...")

    # Statute example
    create_stub_pdf(
        "statute-inheritance-act-1975.pdf",
        "Inheritance (Provision for Family and Dependants) Act 1975",
        """This is a stub document for testing purposes.

The actual Inheritance (Provision for Family and Dependants) Act 1975
can be found at:
https://www.legislation.gov.uk/ukpga/1975/63

This Act enables certain categories of people to apply for reasonable
financial provision from the estate of a deceased person.

Key sections include:
- Section 1: Applications for financial provision
- Section 2: Powers of court to make orders
- Section 3: Matters to which court is to have regard""",
        REFERENCES_DIR / "legislation",
    )

    # Case example
    create_stub_pdf(
        "case-ilott-v-mitson-2017.pdf",
        "Ilott v Mitson and others [2017] UKSC 17",
        """This is a stub document for testing purposes.

The actual judgment can be found at:
https://www.bailii.org/uk/cases/UKSC/2017/17.html

This Supreme Court case provides important guidance on family provision
claims under the Inheritance Act 1975, particularly regarding claims
by adult children.

The case concerned an adult estranged daughter who was left nothing
in her mother's will.""",
        REFERENCES_DIR / "cases",
    )

    # Form example
    create_stub_pdf(
        "form-n1-claim-form.pdf",
        "Form N1 - Claim Form",
        """This is a stub document for testing purposes.

The actual Form N1 can be obtained from HMCTS at:
https://www.gov.uk/government/publications/form-n1-claim-form

Form N1 is used to start most types of civil claims in the County Court
and High Court in England and Wales.

For contentious probate matters, this form may be used to bring claims
under the Inheritance Act 1975 or to challenge the validity of a will.""",
        REFERENCES_DIR / "forms",
    )

    print("\n✓ Stub PDF creation complete!")


if __name__ == "__main__":
    main()
