from rest_framework import serializers

from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    name_len = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        # fields = ['id', 'name', 'description']
        fields = "__all__"

    def get_name_len(self, object):
        return len(object.name)

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description should be different')

        return data