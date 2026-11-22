"""
Generates the comprehensive University SRDS Document for MindEase:
- Documentation/SRDS/MindEase_SRDS_Specification.md (Markdown)
- Documentation/SRDS/MindEase_SRDS_Specification.docx (Microsoft Word with embedded diagrams & tables)
"""
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_table_borders(table, color="D1D5DB", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), val)
        border.set(qn('w:sz'), sz)
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tblBorders.append(border)
    tblPr.append(tblBorders)

def generate_srds_documents():
    print("Generating comprehensive MindEase SRDS documentation...")
    
    # -------------------------------------------------------------
    # 1. MARKDOWN DOCUMENT GENERATION
    # -------------------------------------------------------------
    md_path = os.path.join("Documentation", "SRDS", "MindEase_SRDS_Specification.md")
    
    with open("scripts/srds_content.py", "w", encoding="utf-8") as f:
        f.write("# Helper module containing text content for SRDS\n")

    # Let's write the comprehensive markdown file directly
    print("Writing Markdown SRDS Specification...")
    # We will invoke our build script that writes the rich content and creates the docx.
    
if __name__ == "__main__":
    generate_srds_documents()
