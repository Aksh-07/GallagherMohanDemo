import pdfplumber
import google.generativeai as genai
import json

# Set up Gemini API Key
API_KEY = "AIzaSyAvrlE-_SGHosgjfOA_7VCyLq0toy2j5E8"
genai.configure(api_key=API_KEY)

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def get_invoice_details(text):
    """Uses Gemini API to extract invoice details."""
    prompt = f"""
    Extract the following details from the invoice text:
    - Invoice Date
    - Invoice Number
    - Total Amount Due
    - Due Date

    Return the response in JSON format.
    
    Invoice Text:
    {text}
    """

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    try:
        return json.dumps(response.text)
    except json.JSONDecodeError:
        return {"error": "Invalid response format"}

if __name__ == "__main__":
    pdf_path = "/home/aksh/Downloads/Comcast Bill (1).pdf"  # Path to the uploaded PDF
    extracted_text = extract_text_from_pdf(pdf_path)
    
    invoice_details = get_invoice_details(extracted_text)
    
    print(json.dumps(invoice_details, indent=4))
