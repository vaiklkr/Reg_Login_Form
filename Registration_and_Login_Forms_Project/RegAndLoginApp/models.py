from django.db import models

class Reg(models.Model):
    user = models.CharField(primary_key=True, max_length=64)
    pwd = models.CharField(max_length=64) 
