"""
Shared Diagram Builder utility for MindEase FYP SRDS
Generates standard Draw.io XML and pristine SVG vectors.
"""
import xml.etree.ElementTree as ET
import os

class DrawioBuilder:
    def __init__(self, name, width=1200, height=800):
        self.name = name
        self.width = width
        self.height = height
        self.cells = []
        self.cell_id = 2

    def add_cell(self, value="", style="", vertex="1", parent="1", x=0, y=0, w=100, h=40, edge=None, source=None, target=None, points=None):
        cid = str(self.cell_id)
        self.cell_id += 1
        cell = {
            "id": cid,
            "value": value,
            "style": style,
            "vertex": vertex if not edge else None,
            "edge": "1" if edge else None,
            "parent": parent,
            "x": x, "y": y, "w": w, "h": h,
            "source": source,
            "target": target,
            "points": points
        }
        self.cells.append(cell)
        return cid

    def to_xml(self):
        root = ET.Element("mxfile", host="app.diagrams.net", version="21.0.0", type="device")
        diagram = ET.SubElement(root, "diagram", id=f"diag_{self.name}", name=self.name)
        model = ET.SubElement(diagram, "mxGraphModel", dx=str(self.width), dy=str(self.height), grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth=str(self.width), pageHeight=str(self.height), background="#ffffff", math="0", shadow="0")
        root_cell = ET.SubElement(model, "root")
        
        c0 = ET.SubElement(root_cell, "mxCell", id="0")
        c1 = ET.SubElement(root_cell, "mxCell", id="1", parent="0")
        
        for c in self.cells:
            cell_elem = ET.SubElement(root_cell, "mxCell", id=c["id"], parent=c["parent"])
            if c["value"]:
                cell_elem.set("value", c["value"])
            if c["style"]:
                cell_elem.set("style", c["style"])
            if c.get("vertex"):
                cell_elem.set("vertex", c["vertex"])
            if c.get("edge"):
                cell_elem.set("edge", c["edge"])
            if c.get("source"):
                cell_elem.set("source", c["source"])
            if c.get("target"):
                cell_elem.set("target", c["target"])
                
            geom = ET.SubElement(cell_elem, "mxGeometry")
            if c.get("edge"):
                geom.set("relative", "1")
                geom.set("as", "geometry")
                if c.get("points"):
                    arr = ET.SubElement(geom, "Array", **{"as": "points"})
                    for px, py in c["points"]:
                        ET.SubElement(arr, "mxPoint", x=str(px), y=str(py))
            else:
                geom.set("x", str(c["x"]))
                geom.set("y", str(c["y"]))
                geom.set("width", str(c["w"]))
                geom.set("height", str(c["h"]))
                geom.set("as", "geometry")
                
        return ET.tostring(root, encoding="utf-8", xml_declaration=True).decode("utf-8")

    def save(self, filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        xml_content = self.to_xml()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(xml_content)
        return filepath
