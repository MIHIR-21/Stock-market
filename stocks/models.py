from django.db import models

# Create your models here.
class Add_stocks(models.Model):
    stockname = models.CharField(max_length=100)
    stockprice = models.FloatField()
    mrkcap = models.IntegerField()