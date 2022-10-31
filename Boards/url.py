from django.urls import path
from . import views
urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
    path('boards/<int:board_id>/', views.BoardView.as_view(), name='board_topics'),
    path('boards/<int:board_id>/topics/<int:topic_id>/', views.PostView.as_view(), name='posts'),
    path('boards/new/', views.New_Board.as_view(), name='new_board'),
    path('boards/<int:board_id>/new/', views.New_Topic.as_view(), name='new_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>/new/', views.New_Post.as_view(), name='new_post'),
    
]
