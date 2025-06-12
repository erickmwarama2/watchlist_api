from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    path('', views.movie_list, name='movie-list'),
    path('<int:pk>', views.movie_details, name='movie-details')
]