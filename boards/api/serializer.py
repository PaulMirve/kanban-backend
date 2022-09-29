from rest_framework.serializers import ModelSerializer
from boards.models import Board


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name']

    def create(self, validated_data):
        request = self.context.get('request')
        instance = self.Meta.model(**validated_data)
        if request.user is not None:
            instance.user = request.user
            instance.save()
        return instance
