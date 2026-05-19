import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def compile_legal_pdf(meta: dict, source_url: str, file_hash: str, assessment: str) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=22, spaceAfter=20, textColor=colors.HexColor('#0F172A'))
    body_style = ParagraphStyle('ReportBody', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14, textColor=colors.HexColor('#334155'))
    
    story = [
        Paragraph("DIGITAL EVIDENCE PRESERVATION REPORT", title_style),
        Spacer(1, 10)
    ]
    
    table_data = [
        [Paragraph("System Source URL", body_style), Paragraph(source_url, body_style)],
        [Paragraph("Cryptographic Signature (SHA-256)", body_style), Paragraph(file_hash, body_style)],
        [Paragraph("Timestamp (Local System)", body_style), Paragraph(meta['timestamp_ist'], body_style)],
        [Paragraph("Verification Security Node", body_style), Paragraph(meta['node_identifier'], body_style)]
    ]
    
    meta_table = Table(table_data, colWidths=[200, 300])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 8)
    ]))
    
    story.append(meta_table)
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Case Assessment Log:</b>", body_style))
    story.append(Paragraph(assessment.replace("\n", "<br/>"), body_style))
    
    doc.build(story)
    return buffer.getvalue()
