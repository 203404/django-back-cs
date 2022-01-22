from django.utils import timezone
from django.db import models

# Create your models here.
class primerTabla(models.Model):
    nombre = models.CharField(max_length=50, null= False)
    edad = models.IntegerField(default=0, null= False)
    created = models.DateTimeField(default = timezone.now)
    edit = models.DateTimeField(blank=True, null=True, default=None)