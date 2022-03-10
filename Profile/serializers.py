from dataclasses import fields
from rest_framework import routers, serializers, viewsets
from Profile.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('pk', 'id_user', 'url_img')