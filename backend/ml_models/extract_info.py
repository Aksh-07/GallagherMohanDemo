class PdfExtracter:
    def __init__(self, path: str):
        self.pdf_location = path

    def extract_basic(self):
        # TO DO: train and use ml and llm models to extract information from pdf
        extracted_data = {
            "invoice_date": "2015-12-28",
            "invoice_number": "9384",
            "amount": "108.82",
            "due_date": "2016-01-12",
        }
        return extracted_data

