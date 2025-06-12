from django.urls import path
from watchlist_app.api import views, views_class
from watchlist_app.api.views_class import MovieListAPIView, MovieDetailAPIView

# urlpatterns = [
#     path('', views.movie_list, name='movie-list'),
#     path('<int:pk>', views.movie_details, name='movie-details')
# ]

urlpatterns = [
    path('', MovieListAPIView.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAPIView.as_view(), name='movie-details')
]