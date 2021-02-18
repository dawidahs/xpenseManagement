from django.contrib import admin
from django.urls import path
from my_expenses import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


app_name = 'exp'

urlpatterns = [
    path('', views.home),
    path('upload/', views.upload, name="Upload"),
    #path('upload/', views.expense_form),
    path('index/', views.expenses_list, name="List"),
    path('index/expense_form/', views.expense_form, name="Expense Entry"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.expense_delete, name='expense_delete'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.expense_edit, name='expense_edit'),
]

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)