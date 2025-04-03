from django.db import models


class Invoice(models.Model):
    invoice_date = models.DateField(null=True, blank=True)
    invoice_number = models.BigIntegerField(null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=10)
    due_date = models.DateField(null=True, blank=True)
    pdf_file = models.FileField(null=True, upload_to="invoices/")

    def __str__(self):
        return (
            f"Invoice {self.invoice_number if self.invoice_number is not None else 'None'} | "
            f"Date: {self.invoice_date.strftime('%Y-%m-%d') if self.invoice_date else 'None'} | "
            f"Amount: {self.amount if self.amount is not None else 'None'} | "
            f"Due: {self.due_date.strftime('%Y-%m-%d') if self.due_date else 'None'}"
        )

    def to_dict(self):
        """Returns invoice details as a dictionary with 'None' for missing values."""
        return {
            "invoice_date": (
                self.invoice_date.strftime("%Y-%m-%d") if self.invoice_date else "None"
            ),
            "invoice_number": (
                self.invoice_number if self.invoice_number is not None else "None"
            ),
            "amount": f"${self.amount}" if self.amount is not None else "None",
            "due_date": self.due_date.strftime("%Y-%m-%d") if self.due_date else "None",
            "pdf_file": self.pdf_file.url if self.pdf_file else "None",
        }

    class Meta:
        db_table = "invoices"
