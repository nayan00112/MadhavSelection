from django.db import models

# Create your models here.

class UplodeItemsDB(models.Model):
    img = models.ImageField(upload_to="uploads/")
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    Size = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)