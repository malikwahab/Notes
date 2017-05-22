from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from notes.serializers import NoteSerializer


# class UserSerializers(ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'first_name', 'last_name', 'email',)
#         read_only_fields = ('username',)
#

class CreateUserSerializers(ModelSerializer):

    notes = NoteSerializer(many=True, read_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name',
                  'email', 'notes')
        extra_kwargs = {'password': {'write_only': True}}
