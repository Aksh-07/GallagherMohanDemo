from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from ml_models.extract_info import PdfExtracter
from pdf_extractor.settings import BASE_DIR

from .forms import UploadPdfForm
from .models import Invoice

def upload_pdf_view(request: HttpRequest) -> HttpResponse:
    form = UploadPdfForm()

    if request.method == "POST":
        form = UploadPdfForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data.get("pdf_file", None)
            invoice = Invoice.objects.create(pdf_file=pdf_file)

            file_path = f"{BASE_DIR}/{invoice.pdf_file}"
            extracted_data = PdfExtracter(path=file_path).extract_basic()

            invoice.invoice_date = extracted_data["invoice_date"]
            invoice.invoice_number = extracted_data["invoice_number"]
            invoice.amount = extracted_data["amount"]
            invoice.due_date = extracted_data["due_date"]
            invoice.save()

            return redirect(reverse("api:parsed_invoice", kwargs={"invoice_id": invoice.id}))
                   

    context = {
        "form": form
    }

    return render(request, "api/upload_pdf.html", context)


def parsed_invoice(request: HttpRequest, invoice_id: int) -> HttpResponse:
    invoice = Invoice.objects.get(id=invoice_id)
    context = {"invoice": invoice}
    return render(request, "api/parsed_invoice.html", context)
