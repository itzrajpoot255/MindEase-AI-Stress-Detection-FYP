"""
Sequence Diagram Engine for MindEase FYP SRDS
Generates professional UML Sequence Diagrams matching the Inspiration PDF layout.
Produces both SVG and native Draw.io XML files.
"""
import os
import xml.etree.ElementTree as ET
from drawio_builder import DrawioBuilder

class SequenceDiagramRenderer:
    def __init__(self, title, figure_caption, participants, steps, width=1050, height=850):
        self.title = title
        self.figure_caption = figure_caption
        self.participants = participants  # list of (pid, label, is_actor)
        self.steps = steps  # list of message / fragment dicts
        self.width = width
        self.height = height

    def generate_svg(self):
        svg_parts = []
        svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}">')
        svg_parts.append('<defs>')
        svg_parts.append('<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/></marker>')
        svg_parts.append('<marker id="async" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10" fill="none" stroke="#0f172a" stroke-width="1.5"/></marker>')
        svg_parts.append('<marker id="return-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10" fill="none" stroke="#334155" stroke-width="1.5"/></marker>')
        svg_parts.append('</defs>')
        
        # Pure white background
        svg_parts.append(f'<rect width="{self.width}" height="{self.height}" fill="#ffffff"/>')

        # Frame border
        frame_x, frame_y = 40, 30
        frame_w, frame_h = self.width - 80, self.height - 90
        svg_parts.append(f'<rect x="{frame_x}" y="{frame_y}" width="{frame_w}" height="{frame_h}" fill="none" stroke="#1e293b" stroke-width="1.5"/>')
        
        # Frame Title box (UML sd tag)
        title_box_w = max(160, len(self.title) * 8.5 + 24)
        svg_parts.append(f'<path d="M {frame_x} {frame_y} L {frame_x + title_box_w} {frame_y} L {frame_x + title_box_w} {frame_y + 22} L {frame_x + title_box_w - 12} {frame_y + 32} L {frame_x} {frame_y + 32} Z" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>')
        svg_parts.append(f'<text x="{frame_x + 10}" y="{frame_y + 20}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">sd {self.title}</text>')

        # Layout participants
        n_p = len(self.participants)
        p_spacing = (frame_w - 140) / (n_p - 1) if n_p > 1 else 200
        p_x_map = {}
        top_box_y = frame_y + 60
        bottom_box_y = frame_y + frame_h - 70

        for i, (pid, label, is_actor) in enumerate(self.participants):
            cx = frame_x + 70 + i * p_spacing
            p_x_map[pid] = cx

            # Lifeline
            svg_parts.append(f'<line x1="{cx}" y1="{top_box_y + (45 if is_actor else 35)}" x2="{cx}" y2="{bottom_box_y}" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5,5"/>')

            # Top Participant shape
            if is_actor:
                # Stick figure
                head_y = top_box_y + 10
                svg_parts.append(f'<circle cx="{cx}" cy="{head_y}" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>')
                svg_parts.append(f'<line x1="{cx}" y1="{head_y + 8}" x2="{cx}" y2="{head_y + 24}" stroke="#0f172a" stroke-width="1.5"/>')
                svg_parts.append(f'<line x1="{cx - 12}" y1="{head_y + 14}" x2="{cx + 12}" y2="{head_y + 14}" stroke="#0f172a" stroke-width="1.5"/>')
                svg_parts.append(f'<line x1="{cx}" y1="{head_y + 24}" x2="{cx - 10}" y2="{head_y + 38}" stroke="#0f172a" stroke-width="1.5"/>')
                svg_parts.append(f'<line x1="{cx}" y1="{head_y + 24}" x2="{cx + 10}" y2="{head_y + 38}" stroke="#0f172a" stroke-width="1.5"/>')
                svg_parts.append(f'<text x="{cx}" y="{top_box_y - 8}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{label}</text>')
                # Bottom actor stick figure
                bhead_y = bottom_box_y + 10
                svg_parts.append(f'<circle cx="{cx}" cy="{bhead_y}" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>')
                svg_parts.append(f'<line x1="{cx}" y1="{bhead_y + 8}" x2="{cx}" y2="{bhead_y + 24}" stroke="#0f172a" stroke-width="1.5"/>')
                svg_parts.append(f'<line x1="{cx - 12}" y1="{bhead_y + 14}" x2="{cx + 12}" y2="{bhead_y + 14}" stroke="#0f172a" stroke-width="1.5"/>')
                svg_parts.append(f'<line x1="{cx}" y1="{bhead_y + 24}" x2="{cx - 10}" y2="{bhead_y + 38}" stroke="#0f172a" stroke-width="1.5"/>')
                svg_parts.append(f'<line x1="{cx}" y1="{bhead_y + 24}" x2="{cx + 10}" y2="{bhead_y + 38}" stroke="#0f172a" stroke-width="1.5"/>')
                svg_parts.append(f'<text x="{cx}" y="{bottom_box_y + 54}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{label}</text>')
            else:
                bw, bh = 110, 32
                svg_parts.append(f'<rect x="{cx - bw/2}" y="{top_box_y}" width="{bw}" height="{bh}" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5" rx="3"/>')
                svg_parts.append(f'<text x="{cx}" y="{top_box_y + 20}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{label}</text>')
                svg_parts.append(f'<rect x="{cx - bw/2}" y="{bottom_box_y}" width="{bw}" height="{bh}" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5" rx="3"/>')
                svg_parts.append(f'<text x="{cx}" y="{bottom_box_y + 20}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{label}</text>')

        # Process steps (messages, fragments, activations)
        current_y = top_box_y + 75
        step_spacing = 42
        activations = {}  # pid -> list of (start_y, end_y)
        open_fragments = []  # list of dicts

        # Pre-pass to compute fragment bounding boxes and coordinates
        message_coords = []
        for step in self.steps:
            stype = step.get('type')
            if stype in ('call', 'return', 'self'):
                message_coords.append((step, current_y))
                current_y += step_spacing
            elif stype == 'frag_start':
                open_fragments.append({'kind': step['kind'], 'cond': step['condition'], 'start_y': current_y - 15, 'dividers': []})
                current_y += 28
            elif stype == 'frag_divider':
                if open_fragments:
                    open_fragments[-1]['dividers'].append((current_y, step['condition']))
                current_y += 28
            elif stype == 'frag_end':
                if open_fragments:
                    frag = open_fragments.pop()
                    frag['end_y'] = current_y + 5
                    # render fragment
                    fx = frame_x + 20
                    fw = frame_w - 40
                    fy = frag['start_y']
                    fh = frag['end_y'] - fy
                    svg_parts.append(f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" fill="#fafbfc" fill-opacity="0.3" stroke="#475569" stroke-width="1.2" rx="2"/>')
                    # tag box
                    svg_parts.append(f'<path d="M {fx} {fy} L {fx + 50} {fy} L {fx + 50} {fy + 16} L {fx + 42} {fy + 22} L {fx} {fy + 22} Z" fill="#e2e8f0" stroke="#475569" stroke-width="1.2"/>')
                    svg_parts.append(f'<text x="{fx + 6}" y="{fy + 14}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">{frag["kind"]}</text>')
                    if frag.get('cond'):
                        svg_parts.append(f'<text x="{fx + 60}" y="{fy + 15}" font-family="Arial, sans-serif" font-size="11" font-style="italic" fill="#1e293b">{frag["cond"]}</text>')
                    for div_y, dcond in frag['dividers']:
                        svg_parts.append(f'<line x1="{fx}" y1="{div_y}" x2="{fx + fw}" y2="{div_y}" stroke="#64748b" stroke-width="1.2" stroke-dasharray="6,4"/>')
                        if dcond:
                            svg_parts.append(f'<text x="{fx + 20}" y="{div_y - 6}" font-family="Arial, sans-serif" font-size="11" font-style="italic" fill="#1e293b">{dcond}</text>')
                current_y += 20

        # Draw messages and activation bars
        # Determine activation bar spans for participants
        for step, my in message_coords:
            stype = step['type']
            from_x = p_x_map[step['from']]
            
            if stype == 'call':
                to_x = p_x_map[step['to']]
                text = step['text']
                # Activation box on target
                svg_parts.append(f'<rect x="{to_x - 6}" y="{my - 5}" width="12" height="32" fill="#ffffff" stroke="#1e293b" stroke-width="1.2"/>')
                # Message line
                svg_parts.append(f'<line x1="{from_x}" y1="{my}" x2="{to_x}" y2="{my}" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>')
                mid_x = (from_x + to_x) / 2
                svg_parts.append(f'<text x="{mid_x}" y="{my - 7}" font-family="Arial, sans-serif" font-size="11" fill="#0f172a" text-anchor="middle">{text}</text>')
            
            elif stype == 'return':
                to_x = p_x_map[step['to']]
                text = step['text']
                svg_parts.append(f'<line x1="{from_x}" y1="{my}" x2="{to_x}" y2="{my}" stroke="#334155" stroke-width="1.3" stroke-dasharray="5,4" marker-end="url(#return-arrow)"/>')
                mid_x = (from_x + to_x) / 2
                svg_parts.append(f'<text x="{mid_x}" y="{my - 7}" font-family="Arial, sans-serif" font-size="11" fill="#334155" text-anchor="middle">{text}</text>')
            
            elif stype == 'self':
                text = step['text']
                svg_parts.append(f'<rect x="{from_x - 6}" y="{my - 5}" width="12" height="32" fill="#ffffff" stroke="#1e293b" stroke-width="1.2"/>')
                # loop back arc/lines
                svg_parts.append(f'<path d="M {from_x + 6} {my} L {from_x + 28} {my} L {from_x + 28} {my + 18} L {from_x + 6} {my + 18}" fill="none" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>')
                svg_parts.append(f'<text x="{from_x + 34}" y="{my + 12}" font-family="Arial, sans-serif" font-size="11" fill="#0f172a" text-anchor="start">{text}</text>')

        # Bottom Caption matching inspiration format
        caption_y = self.height - 35
        svg_parts.append(f'<text x="{self.width / 2}" y="{caption_y}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{self.figure_caption}</text>')

        svg_parts.append('</svg>')
        return "\n".join(svg_parts)

    def generate_drawio(self):
        builder = DrawioBuilder(self.title, self.width, self.height)
        # Background frame
        builder.add_cell(f"sd {self.title}", "shape=umlFrame;whiteSpace=wrap;html=1;width=180;height=30;fillColor=#ffffff;strokeColor=#1e293b;strokeWidth=1.5;fontFamily=Arial;fontSize=12;fontStyle=1;", x=40, y=30, w=self.width-80, h=self.height-90)
        
        # Add participants
        n_p = len(self.participants)
        p_spacing = (self.width - 220) / (n_p - 1) if n_p > 1 else 200
        p_cells = {}
        top_y = 90
        lifeline_h = self.height - 240

        for i, (pid, label, is_actor) in enumerate(self.participants):
            cx = 110 + i * p_spacing
            if is_actor:
                # Actor shape
                cid = builder.add_cell(label, "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=cx-18, y=top_y, w=36, h=55)
            else:
                cid = builder.add_cell(label, "shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#f8fafc;strokeColor=#1e293b;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;size=32;", x=cx-55, y=top_y, w=110, h=lifeline_h)
            p_cells[pid] = cid

        # Add steps as edges / notes
        cur_y = top_y + 80
        for step in self.steps:
            stype = step.get('type')
            if stype == 'call':
                src = p_cells.get(step['from'])
                tgt = p_cells.get(step['to'])
                builder.add_cell(step['text'], "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", edge=True, source=src, target=tgt)
                cur_y += 40
            elif stype == 'return':
                src = p_cells.get(step['from'])
                tgt = p_cells.get(step['to'])
                builder.add_cell(step['text'], "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;strokeColor=#334155;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", edge=True, source=src, target=tgt)
                cur_y += 40
            elif stype == 'self':
                src = p_cells.get(step['from'])
                builder.add_cell(step['text'], "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", edge=True, source=src, target=src)
                cur_y += 40
            elif stype == 'frag_start':
                builder.add_cell(f"{step['kind']} {step.get('condition', '')}", "shape=umlFrame;whiteSpace=wrap;html=1;width=80;height=20;fillColor=none;strokeColor=#475569;strokeWidth=1.2;fontFamily=Arial;fontSize=10;", x=60, y=cur_y, w=self.width-120, h=100)
                cur_y += 25

        return builder.to_xml()
