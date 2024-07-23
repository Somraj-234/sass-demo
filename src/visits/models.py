from django.db import models

# Create your models here.
class PageVisits(models.Model):
    # db -> table
    #id - primary key
    path = models.TextField(blank=True, null=True) # col
    timestamps = models.DateField(auto_now_add=True) # col