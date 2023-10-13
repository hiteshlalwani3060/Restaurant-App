from django.db import models
from django.contrib.auth.models import User
MEAL_TYPE= (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', "Main Dishes"),
    ('desserts', 'Desserts')
)
STATUS = (
    (0, "Unavaible"),
    (1,"Available")
)

class Item(models.Model):
    meal= models.CharField(max_length=1000, unique=True)
    discription= models.CharField(max_length=1500)
    price= models.DecimalField(decimal_places=2, max_digits=10)
    meal_type= models.CharField(choices=MEAL_TYPE, max_length=100)
    author= models.ForeignKey(User,on_delete=models.PROTECT)
    status= models.IntegerField(choices=STATUS, default=1)
    date_created= models.DateTimeField(auto_now_add=True)
    date_updated= models.DateField(auto_now=True)

