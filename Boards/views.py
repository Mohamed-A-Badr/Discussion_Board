from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *

# Create your views here.

class HomeView(View):
    boards = BoardData.objects.all()
    def get(self, request):
        return render(request, 'home.html', {'boards': self.boards})
