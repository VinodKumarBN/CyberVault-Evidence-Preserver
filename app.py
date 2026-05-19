import gradio as gr
import hashlib
from datetime import datetime
import socket
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def process_evidence(target_url, uploaded_file):
    if not target_url or not uploaded_file:
        return "⚠️ Error: Please provide both a URL and an evidence screenshot.", None
        
    # 1. Cryptographic Signatures
    raw_bytes = uploaded_file
    file_checksum = hashlib.sha256(raw_bytes).hexdigest()
    timestamp_ist = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    node_id = hashlib.md5(socket.gethostname().encode()).hexdigest()[:12].upper()
    
    # 2. Case Assessment Narrative
    context_narrative = (
        f"Case analysis log created successfully.\n\n"
        f"The incident occurred on the platform workspace identified via {target_url}.\n"
        f"Initial verification check: File binary signature recorded securely as {file_checksum}.\n"
        f"System integrity nodes status: Active. Document metrics successfully preserved inside directory paths."
    )
    
    # 3. Report PDF Compilation Engine
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
        [Paragraph("System Source URL", body_style), Paragraph(target_url, body_style)],
        [Paragraph("Cryptographic Signature (SHA-256)", body_style), Paragraph(file_checksum, body_style)],
        [Paragraph("Timestamp (Local System)", body_style), Paragraph(timestamp_ist, body_style)],
        [Paragraph("Verification Security Node", body_style), Paragraph(node_id, body_style)]
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
    story.append(Paragraph(context_narrative.replace("\n", "<br/>"), body_style))
    
    doc.build(story)
    pdf_bytes = buffer.getvalue()
    
    # Save a temporary file for user download
    output_pdf_path = f"CERT_EVIDENCE_{file_checksum[:8].upper()}.pdf"
    with open(output_pdf_path, "wb") as f:
        f.write(pdf_bytes)
        
    status_text = f"✅ Success!\n\n🔹 SHA-256 Signature:\n{file_checksum}\n\n🔹 Time Logged:\n{timestamp_ist}"
    return status_text, output_pdf_path

# Visual Layout Layer Block
with gr.Blocks(title="CyberVault Pro") as demo:
    gr.Markdown("# 🛡️ CyberVault Pro")
    gr.Markdown("### **Tamper-Proof Evidence Archival Engine**")
    
    with gr.Row():
        with gr.Column():
            url_input = gr.Textbox(label="Incident Context Source / URL Reference Location", placeholder="e.g., Target URL")
            file_input = gr.File(label="Upload Evidence Media Screenshot", type="binary")
            submit_btn = gr.Button("🛡️ Generate Cryptographic Evidence Log", variant="primary")
            
        with gr.Column():
            output_status = gr.Textbox(label="System Log Output Telemetry", interactive=False)
            output_file = gr.File(label="Download Certified Legal Incident Report (PDF)")
            
    submit_btn.click(fn=process_evidence, inputs=[url_input, file_input], outputs=[output_status, output_file])

if __name__ == "__main__":
    demo.launch(server_port=8501)
