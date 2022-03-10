from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, null = False, blank=False)
    url_img = models.ImageField(
        null=True, blank=True, default='assets/img/default.png', upload_to='img/')
