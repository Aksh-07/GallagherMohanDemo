from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from ml_models.extract_info import PdfExtracter
from pdf_extractor.settings import BASE_DIR

from .forms import UploadPdfForm
from .models import Invoice


def convert_date_format(date_str):
    """Converts MM/DD/YY or similar formats to YYYY-MM-DD."""
    if not date_str:
        return None  # Handle missing dates gracefully
    try:
        return datetime.strptime(date_str, "%m/%d/%y").strftime("%Y-%m-%d")
    except ValueError:
        return None  # Return None if the format is incorrect


def convert_amount(amount_str):
    """Removes '$' and converts to decimal."""
    if not amount_str:
        return None
    try:
        return float(amount_str.replace("$", "").strip())
    except ValueError:
        return None  # Return None if conversion fails


@login_required
def upload_pdf_view(request: HttpRequest) -> HttpResponse:
    form = UploadPdfForm()

    if request.method == "POST":
        form = UploadPdfForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data.get("pdf_file", None)
            invoice = Invoice.objects.create(pdf_file=pdf_file)

            # Process PDF
            file_path = f"{BASE_DIR}/media/{invoice.pdf_file}"
            extracted_data = PdfExtracter(path=file_path).get_invoice_details()

            # Convert and store extracted data
            invoice.invoice_date = convert_date_format(
                extracted_data.get("invoice_date")
            )
            invoice.due_date = convert_date_format(extracted_data.get("due_date"))
            invoice.invoice_number = extracted_data.get("invoice_number") or None
            invoice.amount = convert_amount(extracted_data.get("total_amount_due"))

            invoice.save()

            return redirect(
                reverse("api:parsed_invoice", kwargs={"invoice_id": invoice.id})
            )

    context = {"form": form}
    return render(request, "api/upload_pdf.html", context)


@login_required
def parsed_invoice(request: HttpRequest, invoice_id: int) -> HttpResponse:
    invoice = Invoice.objects.get(id=invoice_id)
    context = {"invoice": invoice}
    return render(request, "api/parsed_invoice.html", context)
