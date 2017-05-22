from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
from notes.models import Note


class NoteSerializer(ModelSerializer):

    owner = ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        content = validated_data.get('content')
        if len(content) > 140:
            raise ValidationError("Content Cannot be more than 140")
        return super(NoteSerializer, self).create(validated_data)

    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'is_private', 'create_at', 'updated_at', 'owner', )
