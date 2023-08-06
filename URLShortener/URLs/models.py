from django.db import models
from django.forms import forms
from datetime import date
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class short_url(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid4 , editable=False)
    short_url = models.CharField(max_length=7 , blank=True , null=True , unique=True )
    long_url = models.CharField(max_length=2048 , blank=False , null= False)
    created_date = models.DateField(default=date.today)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    visits = models.PositiveIntegerField(default=0, blank=True , null = False)

    def __str__(self):
        return str(self.id)
    



class server_counter(models.Model):
    counter = models.PositiveBigIntegerField(blank=False , null=False)
    counter_limit = models.PositiveBigIntegerField(blank=False , null=False)

    def __str__(self):
        return str(self.counter)