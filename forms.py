from django import forms
from .models import Expense

class expenseEntry(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('expense_name', 'description', 'category', 'recepit_date', 'receipt_num', 'total', 'vat_perc', 'vat_amount', 'subtotal', 'vendor_name', 'vendor_vat', 'vendor_address', 'country', 'attachment')

