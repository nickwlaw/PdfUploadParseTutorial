import gradio as gr
from pypdf import PdfReader


def upload_pdf(pdf):
    file_path = pdf.name
    return file_path


def parse_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    page = reader.pages[0]
    text = page.extract_text()
    return text


def upload_parse_pdf(pdf):
    path = upload_pdf(pdf)
    text = parse_pdf(path)
    return text


inputs = gr.File(
    label="Upload a PDF",
    file_types=[".pdf"]
)
outputs = gr.outputs.Textbox(
    label="View extracted PDF text here"
)

gr.Interface(
    fn=upload_parse_pdf,
    inputs=inputs,
    outputs=outputs,
    title="Upload a PDF to extract the text",
).launch()
