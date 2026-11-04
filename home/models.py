from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=225, verbose_name='First Name')
    last_name = models.CharField(max_length=225, verbose_name='Last Name')
    age = models.IntegerField(verbose_name='Age')
    is_active = models.BooleanField(verbose_name='Is Active')