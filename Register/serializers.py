from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=15)
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self,validate_data):
        instace = User()
        instace.username = validate_data.get('username')
        instace.email = validate_data.get('email')
        instace.set_password(validate_data.get('password'))
        instace.save()
        return instace

    def validate_usernames(self,data):
        users = User.objects.filter(username=data)
        if len(users) > 0:
            raise serializers.ValidationError("User already exists")
        else:
            return data