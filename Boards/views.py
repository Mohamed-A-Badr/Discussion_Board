from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import *
from .form import *
from django.utils.decorators import method_decorator


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



class New_Board(View):
    def get(self, request):
        form = NewBoardForm()
        return render(request, 'new_board.html', {'form': form})

    def post(self, request):
        form = NewBoardForm(request.POST)
        form.save()
        return redirect('home')

class New_Topic(View):
    def get(self, request, board_id):
        board = get_object_or_404(BoardData, pk=board_id)
        form = NewTopicForm()
        return render(request, 'new_topic.html', {
            'board': board,
            'form': form
        })

    def post(self, request, board_id):
        form = NewTopicForm(request.POST)
        board = get_object_or_404(BoardData, pk=board_id)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()

            post = PostData.objects.create(
                topic=topic,
                content=form.cleaned_data.get('content'),
                created_by=request.user
            )
            return redirect('board_topics', board_id=board.pk)
        return render(request, 'new_topic.html', {
            'board': board,
            'form': form
        })
