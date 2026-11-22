"""
Renders all SVG diagrams to high-resolution PNGs (300 DPI) and individual PDFs,
and bundles them into a unified publication PDF: Documentation/Diagrams/PDF/All_MindEase_Diagrams.pdf.
"""
import os
import glob
import pymupdf

def render_and_package():
    svg_dir = os.path.join("Documentation", "Diagrams", "SVG")
    png_dir = os.path.join("Documentation", "Diagrams", "PNG")
    pdf_dir = os.path.join("Documentation", "Diagrams", "PDF")
    os.makedirs(png_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)

    svg_files = sorted(glob.glob(os.path.join(svg_dir, "*.svg")))
    print(f"Found {len(svg_files)} SVG files to render...")

    master_pdf = pymupdf.open()
    rendered_count = 0

    # Sort order to ensure logical sequence in Master PDF:
    # 1. 01_System_Architecture to 11_State_Machine_Diagram
    # 2. AD01 to AD05
    # 3. UC01 to UC17
    def sort_key(filepath):
        name = os.path.splitext(os.path.basename(filepath))[0]
        if name.startswith("0") or name.startswith("1"):
            return (1, name)
        elif name.startswith("AD"):
            return (2, name)
        elif name.startswith("UC"):
            return (3, name)
        return (4, name)

    sorted_svg_files = sorted(svg_files, key=sort_key)

    for svg_path in sorted_svg_files:
        base_name = os.path.splitext(os.path.basename(svg_path))[0]
        out_png = os.path.join(png_dir, f"{base_name}.png")
        out_pdf = os.path.join(pdf_dir, f"{base_name}.pdf")

        # Open SVG with pymupdf
        doc = pymupdf.open(svg_path)
        
        # Render high-res PNG (300 DPI)
        pix = doc[0].get_pixmap(dpi=300)
        pix.save(out_png)

        # Convert to PDF
        pdf_bytes = doc.convert_to_pdf()
        pdf_doc = pymupdf.open("pdf", pdf_bytes)
        pdf_doc.save(out_pdf)

        # Append to master PDF
        master_pdf.insert_pdf(pdf_doc)
        pdf_doc.close()
        doc.close()

        rendered_count += 1
        print(f"Rendered [{rendered_count}/{len(sorted_svg_files)}]: {base_name} (PNG: {pix.width}x{pix.height}, PDF)")

    master_pdf_path = os.path.join(pdf_dir, "All_MindEase_Diagrams.pdf")
    master_pdf.save(master_pdf_path)
    master_pdf.close()

    print(f"\n==========================================")
    print(f"Successfully rendered {rendered_count} diagrams.")
    print(f"Master PDF compiled at: {master_pdf_path}")
    print(f"Master PDF size: {os.path.getsize(master_pdf_path)} bytes")
    print(f"==========================================")

if __name__ == "__main__":
    render_and_package()
