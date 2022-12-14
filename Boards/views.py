from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *


# Create your views here.

class HomeView(View):
    boards = BoardData.objects.all()

    def get(self, request):
        return render(request, 'home.html', {'boards': self.boards})


class BoardView(View):
    def get(self, request, board_id):
        board = get_object_or_404(BoardData, pk=board_id)
        topics = board.topic.all()
        return render(request, 'topic.html', {
            'board': board,
            'topics': topics,
        })


class PostView(View):
    def get(self, request, board_id, topic_id):
        topic = get_object_or_404(TopicData, board__pk=board_id, pk=topic_id)
        return render(request, 'post.html', {
            'topic': topic
        })
