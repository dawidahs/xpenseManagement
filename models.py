from django.db import models

# Create your models here.
class MyExpenses(models.Model):
    FLIGHTS = "FL"
    MEALS = "ML"
    INTERNET = "IT"
    PHONE = "PH"
    SOCIAL_SECURITY = "SS"
    CATEGORY_CHOICES = (
        (FLIGHTS, "Flights"),
        (MEALS, "Meals"),
        (INTERNET, "Internet"),
        (PHONE, "Phone Bill"),
        (SOCIAL_SECURITY, "Social Security"),        
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=MEALS)
    image = models.CharField(max_length=100)

