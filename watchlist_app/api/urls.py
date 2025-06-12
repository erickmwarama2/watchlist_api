from django.urls import path
# from watchlist_app.api import views, views_class
from watchlist_app.api.views_class import StreamPlatformAPIView, WatchListAPIView, WatchListDetailAPIView, StreamPlatformDetailsAPIView

# urlpatterns = [
#     path('', views.movie_list, name='movie-list'),
#     path('<int:pk>', views.movie_details, name='movie-details')
# ]

urlpatterns = [
    path('', WatchListAPIView.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailAPIView.as_view(), name='movie-details'),
    path('platforms/', StreamPlatformAPIView.as_view(), name='platforms'),
    path('platforms/<int:pk>', StreamPlatformDetailsAPIView.as_view(), name='platform-details')
]