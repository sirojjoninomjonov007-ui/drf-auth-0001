from rest_framework.serializers import ModelSerializer
from apps.users.models import User


class UserSeralizer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSeralizer(ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','passwor']