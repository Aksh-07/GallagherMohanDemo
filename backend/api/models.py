from django.db import models


class Invoice(models.Model):
    invoice_date = models.DateField(null=True, blank=True)
    invoice_number = models.BigIntegerField(null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=5)
    due_date = models.DateField(null=True, blank=True)
    pdf_file = models.FileField(null=True, upload_to="invoices/")

    def __str__(self):
        return str(self.invoice_number)
    
    class Meta:
        db_table = "invoices"
