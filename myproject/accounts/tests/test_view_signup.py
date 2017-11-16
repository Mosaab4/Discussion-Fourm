# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.core.urlresolvers import reverse

from django.urls import resolve


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ..views import signup
from ..forms import SignUpForm
# Create your tests here.

class SignUpTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    # def test_signup_url_resolves_signup_view(self):
    #     view = resolve('/signup/')
    #     self.assertEquals(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contins_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)

    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)

    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username','email','password1','password2']
        actual = list(form.fields)
        self.assertSequenceEqual(actual,expected)
    
class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'mosaab',
            'email': 'mm@dmd.com',
            'password1': 'abcdef12345',
            'password2': 'abcdef12345',
        }
        self.response = self.client.post(url,data)
        self.home_url = reverse('home')

    def test_redirection(self):
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())
    
    def tses_user_authentication(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

class InvalidSetupTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url , {})

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_users(self):
        self.assertFalse(User.objects.exists())