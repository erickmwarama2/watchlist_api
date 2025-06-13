from rest_framework import viewsets
from rest_framework.response import Response

from watchlist_app.api.model_serializers import StreamPlatformSerializer
from watchlist_app.models import StreamPlatform


class StreamPlatformViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.get(pk=pk)
        # StreamPlatform.objects.
        serializer = StreamPlatformSerializer(queryset)
        return Response(serializer.data)