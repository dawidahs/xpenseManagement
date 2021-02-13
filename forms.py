from django import forms
from .models import Expense
from .widgets import BootstrapDateTimePickerInput

class expenseEntry(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('expense_name', 'description', 'category', 'recepit_date', 'receipt_num', 'total', 'vat_perc', 'vat_amount', 'subtotal', 'vendor_name', 'vendor_vat', 'vendor_address', 'country', 'attachment')
        widgets = {
            'expense_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'category' : forms.TextInput(attrs={'class': 'form-control'}),
            'receipt_num' : forms.NumberInput(attrs={'class': 'form-control'}),
            'total' : forms.NumberInput(attrs={'class': 'form-control'}),
            'vat_perc' : forms.NumberInput(attrs={'class': 'form-control'}),
            'vat_amount' : forms.NumberInput(attrs={'class': 'form-control'}),
            'subtotal' : forms.NumberInput(attrs={'class': 'form-control'}),
            'vendor_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'vendor_vat' : forms.TextInput(attrs={'class': 'form-control'}),
            'vendor_address' : forms.TextInput(attrs={'class': 'form-control'}),
            'country' : forms.TextInput(attrs={'class': 'form-control'}),
            'attachment' : forms.FileInput(attrs={'class': 'form-control-file'}),
            'receipt_date' : forms.DateTimeField(
                input_formats=['%d/%m/%Y'], 
                widget=BootstrapDateTimePickerInput(),
                )
        }
