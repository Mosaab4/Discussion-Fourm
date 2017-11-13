# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse , Http404
# Create your views here.

from .models import Board, Topic, Post
from django.contrib.auth.models import User

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

    if request.method == 'POST' :
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()

        topic = Topic.objects.create(
            subject = subject,
            board= board,
            starter= user
        )

        post = Post.objects.create(
            message = message,
            topic = topic,
            created_by = user   
        )

        return redirect('board_topics', pk=board.pk)

    context = {
        'board': board,
    }

    return render(request,'new_topic.html', context)
