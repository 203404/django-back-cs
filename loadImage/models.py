from django.db import models
from django.utils import timezone

# Create your models here.
class LoadImage(models.Model):
    name_img = models.CharField(max_length=15, null = True)
    url_img = models.ImageField(null=True,blank=True, default='', upload_to='assets/img/')
    format_img = models.CharField(max_length=15, null = True)
    created = models.DateTimeField(default = timezone.now)
    edited =  models.DateTimeField(blank=True, null=True, default=None) 
    
    class Meta:
        managed: True
        db_table: 'loadImage'