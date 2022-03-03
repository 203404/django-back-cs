""" from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=15)
    email = serializers.CharField()
    password = serializers.CharField()
    #crea el usuario
    def create(self,validate_data):
        instace = User()
        instace.username = validate_data.get('username')
        instace.email = validate_data.get('email')
        instace.set_password(validate_data.get('password'))
        instace.save()
        return instace

    #valida la existencia del usuario
    def validate_usernames(self,data):
        users = User.objects.filter(username=data)
        if len(users) > 0:
            raise serializers.ValidationError("User already exists")
        else:
            return data """

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
   email = serializers.EmailField(
           required=True,
           validators=[UniqueValidator(queryset=User.objects.all())]
           )
 
   password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
   password2 = serializers.CharField(write_only=True, required=True)
 
   class Meta:
       model = User
       fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
       extra_kwargs = {
           'first_name': {'required': True},
           'last_name': {'required': True}
       }
 
   def validate(self, attrs):
       if attrs['password'] != attrs['password2']:
           raise serializers.ValidationError({"password": "Password fields didn't match."})
 
       return attrs
 
   def create(self, validated_data):
       user = User.objects.create(
           username=validated_data['username'],
           email=validated_data['email'],
           first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
       )
 
      
       user.set_password(validated_data['password'])
       user.save()
 
       return user