from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('start', views.start, name='start'),
    path('choose_move', views.choose_move, name='choose_move'),
    path('list_all_matches', views.MatchesList.as_view(), name='list_all_matches'),
    path('matches_history',views.matches_history, name='matches_history'),
    path('match_detail/<int:match_id>/', views.MatchDetail.as_view()),
]
