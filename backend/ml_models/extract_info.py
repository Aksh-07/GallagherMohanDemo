import json
import os

import google.generativeai as genai
import pdfplumber
from dotenv import load_dotenv


class PdfExtracter:
    # Load environment variables from .env
    load_dotenv()

    # Set up Gemini API Key
    API_KEY = os.getenv("GEMINI_API_KEY")

    if not API_KEY:
        raise ValueError("API Key is missing! Set GEMINI_API_KEY in .env")

    genai.configure(api_key=API_KEY)

    def __init__(self, path: str):
        self.pdf_location = path
        self.text = self.extract_text_from_pdf()

    def extract_text_from_pdf(self):
        """Extracts text from a PDF file."""
        text = ""
        with pdfplumber.open(self.pdf_location) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    def get_invoice_details(self):
        """Uses Gemini API to extract invoice details."""

        prompt = f"""
        Extract the following details from the invoice text:
        - invoice_date
        - invoice_number
        - total_amount_due
        - due_date


        Return the response in a valid JSON format without any markdown, code blocks, or extra text.

        Invoice Text:
        {self.text}
        """

        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)

        try:
            # Clean response by removing markdown formatting
            cleaned_text = response.text.strip("```json").strip("```").strip()

            # Convert cleaned text into a dictionary
            return json.loads(cleaned_text)
        except json.JSONDecodeError:
            return {"error": "Invalid response format"}


# if __name__ == "__main__":
#     pdf_path = "/home/aksh/aksh_code/GallagherMohanDemo/backend/invoices/Comcast_Bill_1_fIGEZm8.pdf"  # Path to the uploaded PDF

#     invoice_details = get_invoice_details(extracted_text)
#     print(invoice_details)
