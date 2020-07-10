from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from my_expenses.models import MyExpenses

# Create your views here.
def home(request):
    return render(request, 'my_expenses/base.html',)

def expenses_list(request):
    all_expenses = MyExpenses.objects.all()
    return render(request, 'my_expenses/index.html', {'all_expenses': all_expenses})

def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'my_expenses/upload.html', context)
