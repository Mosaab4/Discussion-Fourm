# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse , Http404
# Create your views here.

from .models import Board

def home(request):
    boards = Board.objects.all()
    context = {
        'boards':boards,
    }
    return render(request,'home.html',context)

def board_topics(request, pk):
  
    board = get_object_or_404(Board, pk=pk)
    
    context = {
        'board':board,
    }

    return render(request,"topics.html",context)

def new_topic(request,pk):
    board = get_object_or_404(Board, pk=pk)

    context = {
        'board': board,
    }

    return render(request,'new_topic.html', context)
