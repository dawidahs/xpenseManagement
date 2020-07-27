from django.db import models
from django.utils import timezone

class Expense(models.Model):
    expense_name = models.CharField(max_length=100, default="Expense Name")
    description = models.CharField(max_length=240)  
    recepit_date = models.DateField(max_length=10)
    receipt_num = models.CharField(max_length=32, default="1")
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vat_perc = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vat_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vendor_name = models.CharField(max_length=100, default="Vendor")
    vendor_vat = models.CharField(max_length=20, default=" ")
    vendor_address = models.CharField(max_length=100, default="address")
    country = models.CharField(max_length=30, default="España")
    category = models.CharField(max_length=100, default="category")
    attachment = models.FileField(upload_to="receipts/")

    def __str__(self) -> str:
        return self.expense_name

# Create your models here.
"""class MyExpenses(models.Model):
    expense_name = models.CharField(max_length=100, default="Expense Name")
    description = models.CharField(max_length=240, default="Description")  
    recepit_date = models.DateField(max_length=10, default=timezone.now)
    receipt_num = models.CharField(max_length=32, default="1")
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vat_perc = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vat_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vendor_name = models.CharField(max_length=100, default="Vendor")
    vendor_vat = models.CharField(max_length=20, default=" ")
    vendor_address = models.CharField(max_length=100, default="address")
    country = models.CharField(max_length=30, default="España")
    category = models.CharField(max_length=100, default="category")
    attachment = models.FileField(upload_to="receipts/")

    def __str__(self) -> str:
        return self.expense_name"""


