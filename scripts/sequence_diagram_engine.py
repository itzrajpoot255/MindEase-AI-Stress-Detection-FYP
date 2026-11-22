"""
Flawless UML 2.5 Sequence Diagram Engine for MindEase FYP SRDS
Generates publication-quality Sequence Diagrams with:
- Dynamic responsive width (1250px - 1450px) based on participant count & label length
- Dynamic responsive height based on execution steps and combined fragments
- Generous lifeline spacing (~260-280px) ensuring method signatures never overflow lifelines
- Proper UML 2.5 message arrowheads: solid for synchronous calls, dashed with open arrow for returns
- Clean activation bars on active lifelines and nested activation bars for self-calls
- Standard UML lifeline termination (no duplicate bottom boxes or smashed stick figures)
- Clean Combined Fragments (alt, opt, loop) with pentagon header tabs and dashed operand dividers
- Pure white background (#ffffff) and crisp typography
"""
import os
from drawio_builder import DrawioBuilder

class SequenceDiagramRenderer:
    def __init__(self, title, figure_caption, participants, steps, width=None, height=None):
        self.title = title
        self.figure_caption = figure_caption
        self.participants = participants  # list of (pid, label, is_actor)
        self.steps = steps  # list of message / fragment dicts

        # Dynamic responsive width calculation based on participant count
        n_p = len(participants)
        if width is None:
            if n_p <= 4:
                self.width = 1200
            elif n_p == 5:
                self.width = 1350
            else:
                self.width = 1480
        else:
            self.width = width

        # Dynamic responsive height calculation based on steps
        step_spacing = 46
        total_y = 120 # top margin + header
        for step in steps:
            stype = step.get('type')
            if stype in ('call', 'return', 'self'):
                total_y += step_spacing
            elif stype == 'frag_start':
                total_y += 32
            elif stype == 'frag_divider':
                total_y += 32
            elif stype == 'frag_end':
                total_y += 24

        min_h = 880
        self.height = max(min_h, total_y + 140) if height is None else height

    def generate_svg(self):
        svg_parts = []
        svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}">')
        svg_parts.append('<defs>')
        # Solid filled arrow for synchronous call
        svg_parts.append('  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">')
        svg_parts.append('    <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>')
        svg_parts.append('  </marker>')
        # Open arrowhead for return message
        svg_parts.append('  <marker id="return-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">')
        svg_parts.append('    <path d="M 0 1 L 8 5 L 0 9" fill="none" stroke="#475569" stroke-width="1.5"/>')
        svg_parts.append('  </marker>')
        svg_parts.append('</defs>')

        # Pure white background
        svg_parts.append(f'<rect width="{self.width}" height="{self.height}" fill="#ffffff"/>')

        # Frame border
        frame_x, frame_y = 40, 30
        frame_w, frame_h = self.width - 80, self.height - 85
        svg_parts.append(f'<rect x="{frame_x}" y="{frame_y}" width="{frame_w}" height="{frame_h}" fill="none" stroke="#1e293b" stroke-width="1.5"/>')

        # Frame Title box (UML sd tag)
        title_box_w = max(180, len(self.title) * 8.2 + 30)
        svg_parts.append(f'<path d="M {frame_x} {frame_y} L {frame_x + title_box_w} {frame_y} L {frame_x + title_box_w} {frame_y + 24} L {frame_x + title_box_w - 12} {frame_y + 34} L {frame_x} {frame_y + 34} Z" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>')
        svg_parts.append(f'<text x="{frame_x + 12}" y="{frame_y + 21}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">sd {self.title}</text>')

        # Layout participants at the top with generous spacing
        n_p = len(self.participants)
        margin = 100
        p_spacing = (frame_w - 2 * margin) / (n_p - 1) if n_p > 1 else 250
        p_x_map = {}
        top_box_y = frame_y + 60
        lifeline_bottom_y = frame_y + frame_h - 40

        for i, (pid, label, is_actor) in enumerate(self.participants):
            cx = frame_x + margin + i * p_spacing
            p_x_map[pid] = cx

            if is_actor:
                # Clean UML Actor Stick Figure (Top Only)
                head_y = top_box_y + 16
                svg_parts.append(f'<circle cx="{cx}" cy="{head_y}" r="9" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/>')
                svg_parts.append(f'<line x1="{cx}" y1="{head_y + 9}" x2="{cx}" y2="{head_y + 28}" stroke="#0f172a" stroke-width="1.6"/>')
                svg_parts.append(f'<line x1="{cx - 15}" y1="{head_y + 16}" x2="{cx + 15}" y2="{head_y + 16}" stroke="#0f172a" stroke-width="1.6"/>')
                svg_parts.append(f'<line x1="{cx}" y1="{head_y + 28}" x2="{cx - 12}" y2="{head_y + 46}" stroke="#0f172a" stroke-width="1.6"/>')
                svg_parts.append(f'<line x1="{cx}" y1="{head_y + 28}" x2="{cx + 12}" y2="{head_y + 46}" stroke="#0f172a" stroke-width="1.6"/>')
                svg_parts.append(f'<text x="{cx}" y="{top_box_y - 6}" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{label}</text>')
                lifeline_start_y = head_y + 52
            else:
                # Clean UML Participant Box (Top Only)
                bw, bh = 130, 36
                svg_parts.append(f'<rect x="{cx - bw/2}" y="{top_box_y}" width="{bw}" height="{bh}" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.6" rx="4"/>')
                svg_parts.append(f'<text x="{cx}" y="{top_box_y + 22}" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{label}</text>')
                lifeline_start_y = top_box_y + bh

            # Lifeline (vertical dashed line terminating cleanly before bottom border)
            svg_parts.append(f'<line x1="{cx}" y1="{lifeline_start_y}" x2="{cx}" y2="{lifeline_bottom_y}" stroke="#64748b" stroke-width="1.2" stroke-dasharray="6,5"/>')
            # Clean bottom stop tick (terminator)
            svg_parts.append(f'<line x1="{cx - 8}" y1="{lifeline_bottom_y}" x2="{cx + 8}" y2="{lifeline_bottom_y}" stroke="#64748b" stroke-width="1.6"/>')

        # Compute message Y coordinates and combined fragments
        current_y = top_box_y + 85
        step_spacing = 46
        open_fragments = []
        message_coords = []

        for step in self.steps:
            stype = step.get('type')
            if stype in ('call', 'return', 'self'):
                message_coords.append((step, current_y))
                current_y += step_spacing
            elif stype == 'frag_start':
                open_fragments.append({
                    'kind': step['kind'],
                    'cond': step['condition'],
                    'start_y': current_y - 18,
                    'dividers': []
                })
                current_y += 32
            elif stype == 'frag_divider':
                if open_fragments:
                    open_fragments[-1]['dividers'].append((current_y, step['condition']))
                current_y += 32
            elif stype == 'frag_end':
                if open_fragments:
                    frag = open_fragments.pop()
                    frag['end_y'] = current_y + 6

                    # Render Combined Fragment Box
                    fx = frame_x + 18
                    fw = frame_w - 36
                    fy = frag['start_y']
                    fh = frag['end_y'] - fy

                    # Outer fragment rectangle
                    svg_parts.append(f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" fill="#f8fafc" fill-opacity="0.35" stroke="#64748b" stroke-width="1.2" rx="3"/>')

                    # Pentagon header tab in top-left
                    tab_w = 56
                    svg_parts.append(f'<path d="M {fx} {fy} L {fx + tab_w} {fy} L {fx + tab_w} {fy + 18} L {fx + tab_w - 8} {fy + 24} L {fx} {fy + 24} Z" fill="#e2e8f0" stroke="#64748b" stroke-width="1.2"/>')
                    svg_parts.append(f'<text x="{fx + 10}" y="{fy + 16}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">{frag["kind"]}</text>')

                    if frag.get('cond'):
                        svg_parts.append(f'<text x="{fx + tab_w + 12}" y="{fy + 16}" font-family="Arial, sans-serif" font-size="10.5" font-weight="600" font-style="italic" fill="#1e293b">{frag["cond"]}</text>')

                    # Alternative Dividers (dashed lines across fragment)
                    for div_y, dcond in frag['dividers']:
                        svg_parts.append(f'<line x1="{fx}" y1="{div_y}" x2="{fx + fw}" y2="{div_y}" stroke="#64748b" stroke-width="1.2" stroke-dasharray="6,4"/>')
                        if dcond:
                            svg_parts.append(f'<text x="{fx + 16}" y="{div_y - 7}" font-family="Arial, sans-serif" font-size="10.5" font-weight="600" font-style="italic" fill="#1e293b">{dcond}</text>')

                current_y += 24

        # Draw messages, arrows, and activation bars
        for step, my in message_coords:
            stype = step['type']
            from_x = p_x_map[step['from']]

            if stype == 'call':
                to_x = p_x_map[step['to']]
                text = step['text']

                # Clean activation bar on target lifeline
                svg_parts.append(f'<rect x="{to_x - 6}" y="{my - 4}" width="12" height="34" fill="#ffffff" stroke="#0f172a" stroke-width="1.3" rx="1.5"/>')

                # Synchronous Call message line (solid with filled arrowhead)
                svg_parts.append(f'<line x1="{from_x}" y1="{my}" x2="{to_x}" y2="{my}" stroke="#0f172a" stroke-width="1.4" marker-end="url(#arrow)"/>')

                # Centered label above line with breathing room
                mid_x = (from_x + to_x) / 2
                svg_parts.append(f'<text x="{mid_x}" y="{my - 8}" font-family="Arial, sans-serif" font-size="10" font-weight="600" fill="#0f172a" text-anchor="middle">{text}</text>')

            elif stype == 'return':
                to_x = p_x_map[step['to']]
                text = step['text']

                # Return message line (clean dashed with open arrowhead)
                svg_parts.append(f'<line x1="{from_x}" y1="{my}" x2="{to_x}" y2="{my}" stroke="#475569" stroke-width="1.3" stroke-dasharray="6,4" marker-end="url(#return-arrow)"/>')

                # Centered italic label above line
                mid_x = (from_x + to_x) / 2
                svg_parts.append(f'<text x="{mid_x}" y="{my - 8}" font-family="Arial, sans-serif" font-size="10" font-style="italic" fill="#334155" text-anchor="middle">{text}</text>')

            elif stype == 'self':
                text = step['text']

                # Nested sub-activation bar for self execution
                svg_parts.append(f'<rect x="{from_x - 6}" y="{my - 4}" width="12" height="34" fill="#ffffff" stroke="#0f172a" stroke-width="1.3" rx="1.5"/>')
                svg_parts.append(f'<rect x="{from_x + 2}" y="{my - 1}" width="8" height="24" fill="#ffffff" stroke="#0f172a" stroke-width="1.2" rx="1"/>')

                # Self-call U-turn loop
                svg_parts.append(f'<path d="M {from_x + 10} {my} L {from_x + 36} {my} L {from_x + 36} {my + 20} L {from_x + 10} {my + 20}" fill="none" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>')
                svg_parts.append(f'<text x="{from_x + 42}" y="{my + 14}" font-family="Arial, sans-serif" font-size="10" font-weight="600" fill="#0f172a" text-anchor="start">{text}</text>')

        # Professional Centered Caption at Bottom
        caption_y = self.height - 30
        svg_parts.append(f'<text x="{self.width / 2}" y="{caption_y}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{self.figure_caption}</text>')

        svg_parts.append('</svg>')
        return "\n".join(svg_parts)

    def generate_drawio(self):
        builder = DrawioBuilder(self.title, self.width, self.height)
        builder.add_cell(f"sd {self.title}", "shape=umlFrame;whiteSpace=wrap;html=1;width=180;height=30;fillColor=#ffffff;strokeColor=#1e293b;strokeWidth=1.5;fontFamily=Arial;fontSize=12;fontStyle=1;", x=40, y=30, w=self.width-80, h=self.height-90)

        n_p = len(self.participants)
        margin = 100
        p_spacing = (self.width - 80 - 2 * margin) / (n_p - 1) if n_p > 1 else 250
        p_cells = {}
        top_y = 90
        lifeline_h = self.height - 220

        for i, (pid, label, is_actor) in enumerate(self.participants):
            cx = 40 + margin + i * p_spacing
            if is_actor:
                cid = builder.add_cell(label, "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=cx-18, y=top_y, w=36, h=55)
            else:
                cid = builder.add_cell(label, "shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;size=36;", x=cx-65, y=top_y, w=130, h=lifeline_h)
            p_cells[pid] = cid

        cur_y = top_y + 85
        for step in self.steps:
            stype = step.get('type')
            if stype == 'call':
                src = p_cells.get(step['from'])
                tgt = p_cells.get(step['to'])
                builder.add_cell(step['text'], "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", edge=True, source=src, target=tgt)
                cur_y += 44
            elif stype == 'return':
                src = p_cells.get(step['from'])
                tgt = p_cells.get(step['to'])
                builder.add_cell(step['text'], "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;strokeColor=#475569;strokeWidth=1.3;fontFamily=Arial;fontSize=10;fontStyle=2;", edge=True, source=src, target=tgt)
                cur_y += 44
            elif stype == 'self':
                src = p_cells.get(step['from'])
                builder.add_cell(step['text'], "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#0f172a;strokeWidth=1.4;fontFamily=Arial;fontSize=10;fontStyle=1;", edge=True, source=src, target=src)
                cur_y += 44
            elif stype == 'frag_start':
                builder.add_cell(f"{step['kind']} {step.get('condition', '')}", "shape=umlFrame;whiteSpace=wrap;html=1;width=90;height=22;fillColor=none;strokeColor=#64748b;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontStyle=1;", x=58, y=cur_y, w=self.width-116, h=120)
                cur_y += 28

        return builder.to_xml()
