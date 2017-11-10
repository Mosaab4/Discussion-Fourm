# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Board

def home(request):
    boards = Board.objects.all()
    context = {
        'boards':boards,
    }
    return render(request,'home.html',context)

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)

    context = {
        'board':board,
    }

    return render(request,"topics.html",context)
    
