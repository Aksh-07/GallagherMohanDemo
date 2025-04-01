from django.urls import path

from .views import upload_pdf_view, parsed_invoice

app_name = "api"

urlpatterns = [
    path("upload_pdf/", upload_pdf_view, name="upload_pdf"), 
    path("parsed_invoice/<int:invoice_id>/", parsed_invoice, name="parsed_invoice"),
]
