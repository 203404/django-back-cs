from rest_framework import serializers

#import loadImage.models as models
from loadImage.models import LoadImage

class LoadImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoadImage
        fields = ('id','name_img','format_img', 'url_img')