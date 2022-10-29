from django.urls import path
from . import views
urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
    path('boards/<int:board_id>/', views.BoardView.as_view(), name='board_topics')
]
