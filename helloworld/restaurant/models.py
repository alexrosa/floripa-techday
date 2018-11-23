from django.db import models

# Create your models here.


class Restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=False)
    updated = models.DateTimeField(auto_now_add=True)
