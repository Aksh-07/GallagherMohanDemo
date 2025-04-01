from django import forms


class UploadPdfForm(forms.Form):
    pdf_file = forms.FileField()
