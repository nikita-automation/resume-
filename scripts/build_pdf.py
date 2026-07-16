"""Render Resume_EN.md / Resume_DE.md into clean A4 PDFs with reportlab."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

BASE = Path(__file__).resolve().parent.parent
FONT_DIR = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/native"
REGULAR = FONT_DIR / "poppler/poppler/fonts/DejaVuSans.ttf"
BOLD = (
    FONT_DIR
    / "libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype/DejaVuSans-Bold.ttf"
)

pdfmetrics.registerFont(TTFont("DejaVu", str(REGULAR)))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", str(BOLD)))
pdfmetrics.registerFontFamily("DejaVu", normal="DejaVu", bold="DejaVu-Bold", italic="DejaVu", boldItalic="DejaVu-Bold")

ACCENT = colors.HexColor("#1a3e5c")

S = {
    "name": ParagraphStyle("name", fontName="DejaVu-Bold", fontSize=20, leading=24, textColor=ACCENT),
    "role": ParagraphStyle("role", fontName="DejaVu", fontSize=11, leading=14, textColor=colors.HexColor("#444444")),
    "contact": ParagraphStyle("contact", fontName="DejaVu", fontSize=8.5, leading=12, textColor=colors.HexColor("#555555")),
    "h2": ParagraphStyle("h2", fontName="DejaVu-Bold", fontSize=12, leading=15, textColor=ACCENT, spaceBefore=8),
    "h3": ParagraphStyle("h3", fontName="DejaVu-Bold", fontSize=10, leading=13, spaceBefore=4),
    "italic": ParagraphStyle("italic", fontName="DejaVu", fontSize=8.5, leading=11.5, textColor=colors.HexColor("#555555")),
    "body": ParagraphStyle("body", fontName="DejaVu", fontSize=9, leading=12.5),
    "bullet": ParagraphStyle("bullet", fontName="DejaVu", fontSize=9, leading=12.5, leftIndent=5 * mm, bulletIndent=1 * mm),
}


def md_inline(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<link href="\2" color="#1a5c8a">\1</link>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"<i>\1</i>", text)
    return text


def build(md_path: Path, pdf_path: Path) -> None:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    story = []
    for i, raw in enumerate(lines):
        line = raw.rstrip()
        if not line:
            continue
        if line == "---":
            story.append(Spacer(1, 1.5 * mm))
            story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#c9d4dd")))
            story.append(Spacer(1, 1.5 * mm))
        elif line.startswith("# "):
            story.append(Paragraph(md_inline(line[2:]), S["name"]))
        elif line.startswith("## "):
            story.append(Paragraph(md_inline(line[3:]), S["h2"]))
            story.append(Spacer(1, 1 * mm))
        elif line.startswith("### "):
            story.append(Paragraph(md_inline(line[4:]), S["h3"]))
        elif line.startswith("- "):
            story.append(Paragraph(md_inline(line[2:]), S["bullet"], bulletText="•"))
        elif line.startswith("*") and line.endswith("*") and not line.startswith("**"):
            story.append(Paragraph(md_inline(line.strip("*")), S["italic"]))
            story.append(Spacer(1, 1 * mm))
        elif i <= 4 and line.startswith("**"):
            story.append(Paragraph(md_inline(line), S["role"]))
        elif i <= 6 and "·" in line:
            story.append(Paragraph(md_inline(line), S["contact"]))
        else:
            story.append(Paragraph(md_inline(line), S["body"]))
            story.append(Spacer(1, 1 * mm))

    doc = SimpleDocTemplate(
        str(pdf_path), pagesize=A4,
        leftMargin=16 * mm, rightMargin=16 * mm, topMargin=14 * mm, bottomMargin=14 * mm,
    )
    doc.build(story)
    print(f"built {pdf_path}")


if __name__ == "__main__":
    (BASE / "pdf").mkdir(exist_ok=True)
    for name in sys.argv[1:] or ["Resume_EN", "Resume_DE"]:
        build(BASE / f"{name}.md", BASE / "pdf" / f"{name}.pdf")
