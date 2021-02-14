from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Expense
from .forms import expenseEntry

# Create your views here.

def home(request):
    return render(request, 'my_expenses/base.html',)

def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['request', 'my_expenses/upload.html'] = fs.url(name)
    return render(request, 'my_expenses/upload.html', context)

def expenses_list(request):
    all_expenses = Expense.objects.all()
    return render(request, 'my_expenses/index.html', {'all_expenses': all_expenses})

def expenses_edit(request, pk):
    all_expenses = Expense.objects.all()
    return render(request, 'my_expenses/index.html', {'all_expenses': all_expenses})
    
def expense_form(request):
    if request.method == 'POST':
        form = expenseEntry(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'my_expenses/index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = expenseEntry()
    return render(request, 'my_expenses/expense_form.html', {
        'form' : form
        })
