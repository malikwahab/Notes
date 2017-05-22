from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializers(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)
        read_only_fields = ('username',)


class CreateUserSerializers(ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name',
                  'email', )
        extra_kwargs = {'password': {'write_only': True}}
