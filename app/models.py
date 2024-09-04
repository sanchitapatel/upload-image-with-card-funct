from django.db import models

# Create your models here.
class ItemInfo(models.Model):
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField(max_length=200)
    item_image=models.ImageField(upload_to="image")

