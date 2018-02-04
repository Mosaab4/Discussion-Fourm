# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.contrib.auth.models import User

from ..views import home,board_topics, new_topic
from ..models import Board, Topic,Post
from ..forms import NewTopicForm

# Create your tests here.

class BoardTopicsTest(TestCase):
    def setUp(self):
        Board.objects.create(name='django', description='Django board')
    
    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)  

    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('board_topics', kwargs={'pk':1})
        home_page_url = reverse('home')
        new_topic_url = reverse('new_topic' , kwargs= {'pk':1})

        response = self.client.get(board_topics_url)
        
        self.assertContains(response , 'href="{0}"'.format(home_page_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))
        