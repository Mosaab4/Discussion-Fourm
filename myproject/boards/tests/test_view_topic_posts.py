from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board, Topic,Post
from ..views import topic_posts


class TopicPostsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name='Django', description='Django board')
        user = User.objects.create_user(username='john',email='john@doe.com',password='123')
        topic = Topic.objects.create(subject='hello world', board=board, starter=user)
        Post.objects.create(message='lorem ipsum dolor sit', topic=topic,created_by=user)

        url = reverse('topic_posts',kwargs={'pk': board.pk, 'topic_pk':topic.pk})
        # self.response = self.client.get(url)

        def test_status_code(self):
            response = self.client.get(url)
            self.assertEquals(response.status_code, 200)

        def test_view_functions(self):
            view = resolve('/boards/1/topics/1/')
            self.assertEquals(view.func, topic_posts)

