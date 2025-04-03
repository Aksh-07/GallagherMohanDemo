from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import parsed_invoice, upload_pdf_view

app_name = "api"

urlpatterns = [
    path(
        "",
        LoginView.as_view(template_name="api/login.html", next_page="api:upload_pdf"),
        name="login",
    ),  # Home redirects to login
    path(
        "logout/", LogoutView.as_view(next_page="api:login"), name="logout"
    ),  # Redirect to login after logout
    path("upload_pdf/", upload_pdf_view, name="upload_pdf"),  # Require login
    path(
        "parsed_invoice/<int:invoice_id>/", parsed_invoice, name="parsed_invoice"
    ),  # Require login
]
