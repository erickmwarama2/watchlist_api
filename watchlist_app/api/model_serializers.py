from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    title_len = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        # fields = ['id', 'name', 'description']
        fields = "__all__"

    def get_title_len(self, object):
        return len(object.title)

    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError('Name and description should be different')

        return data