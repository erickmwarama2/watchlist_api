from django.urls import path
# from watchlist_app.api import views, views_class
from watchlist_app.api.views_class import (ReviewDetail, StreamPlatformAPIView,
                                           WatchListAPIView, WatchListDetailAPIView,
                                           StreamPlatformDetailsAPIView, ReviewList, ReviewCreate)

# urlpatterns = [
#     path('', views.movie_list, name='movie-list'),
#     path('<int:pk>', views.movie_details, name='movie-details')
# ]

urlpatterns = [
    path('', WatchListAPIView.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailAPIView.as_view(), name='movie-details'),
    path('<int:pk>/reviews', ReviewList.as_view(), name='movie-reviews'),
    path('<int:pk>/reviews/create', ReviewCreate.as_view(), name='create-movie-reviews'),
    path('reviews/<int:pk>', ReviewDetail.as_view(), name='movie-review-details'),
    path('platforms/', StreamPlatformAPIView.as_view(), name='platforms'),
    path('platforms/<int:pk>', StreamPlatformDetailsAPIView.as_view(), name='platform-details'),
    # path('review', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]