from django.contrib import admin
from django.urls import path
from my_expenses import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('upload/', views.upload, name="Upload"),
    path('index/', views.expenses_list, name="Expenses"),
    path('index/expense_form/', views.expense_form, name="Expense Entry"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)