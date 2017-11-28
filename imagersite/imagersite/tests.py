"""Tests for imagersite."""

from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core import mail


class FontendTest(TestCase):
    """Fontend test."""

    def setUp(self):
        """Setup."""
        self.client = Client()

    def test_response_status_code_home(self):
        """Test home response status code."""
        response = self.client.get(reverse_lazy('home'))
        home_response = response.status_code
        self.assertEqual(home_response, 200)

    def test_response_content_home(self):
        """Test home response content."""
        response = self.client.get(reverse_lazy('home'))
        home_response_content = response.content.decode("utf-8")
        self.assertIn('<h1>home</h1>', home_response_content)

    def test_home_uses_base_template(self):
        """Test home uses base template."""
        response = self.client.get(reverse_lazy('home'))
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_response_status_code_login(self):
        """Test login response status code."""
        response = self.client.get(reverse_lazy('login'))
        login_response = response.status_code
        self.assertEqual(login_response, 200)

    def test_response_content_login(self):
        """Test login response content."""
        response = self.client.get(reverse_lazy('login'))
        login_response_content = response.content.decode("utf-8")
        self.assertIn('<h1>Login</h1>', login_response_content)

    def test_login_uses_base_template(self):
        """Test login uses base template."""
        response = self.client.get(reverse_lazy('login'))
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_response_status_code_register(self):
        """Test register response status code."""
        response = self.client.get('/accounts/register/')
        register_response = response.status_code
        self.assertEqual(register_response, 200)

    def test_response_content_register(self):
        """Test register response content."""
        response = self.client.get('/accounts/register/')
        register_response_content = response.content.decode("utf-8")
        self.assertIn('<h1>Register</h1>', register_response_content)

    def test_register_uses_base_template(self):
        """Test register uses base template."""
        response = self.client.get('/accounts/register/')
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_login_not_user(self):
        """Test login response content when not a user."""
        response = self.client.post(reverse_lazy('login'), {'username': ';alskdjflasdf', 'password': 'as;lkdfjlskdjf'})
        login_response = response.content.decode("utf-8")
        self.assertIn('Please enter a correct username and passwor', login_response)

    def test_valid_login(self):
        """Test valid login response redirects home."""
        user = User(username='bob', email='bob@bob.com')
        user.set_password('potatoes')
        user.save()
        response = self.client.post(reverse_lazy('login'), {'username': user.username, 'password': 'potatoes'}, follow=True)
        login_response = response.status_code
        login_response_content = response.content.decode('utf-8')
        self.assertEqual(login_response, 200)
        self.assertIn('<h1>home</h1>', login_response_content)

    def test_post_registration(self):
        """Test registration works and redirects to check email page."""
        data = {
            'username': 'metsfan',
            'password1': 'potatoes',
            'password2': 'potatoes',
            'email': 'mets@woo.com'
        }
        response = self.client.post('/accounts/register/', data, follow=True)
        register_response = response.content.decode('utf-8')
        self.assertIn('Check your email for an activation URL', register_response)

    def test_new_user_in_database(self):
        """Check registration adds new user to database."""
        data = {
            'username': 'metsfan',
            'password1': 'potatoes',
            'password2': 'potatoes',
            'email': 'mets@woo.com'
        }
        self.client.post('/accounts/register/', data, follow=True)
        self.assertTrue(User.objects.count() == 1)
        self.assertFalse(User.objects.first().is_active)

    def test_confirmation_email(self):
        """Test validation email is sent on registration."""
        data = {
            'username': 'metsfan',
            'password1': 'potatoes',
            'password2': 'potatoes',
            'email': 'mets@woo.com'
        }
        self.client.post('/accounts/register/', data, follow=True)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Click the activation link below', mail.outbox[0].message().get_payload())
        self.assertEqual(mail.outbox[0].to[0], 'mets@woo.com')

    def test_confirmation_link_activates_user(self):
        """Test confirmation link sent in email activates user."""
        data = {
            'username': 'metsfan',
            'password1': 'potatoes',
            'password2': 'potatoes',
            'email': 'mets@woo.com'
        }
        self.client.post('/accounts/register/', data, follow=True)
        content = mail.outbox[0].message().get_payload()
        link = content.split('\n\n')[2]
        self.client.get(link)
        user = User.objects.get(username='metsfan')
        self.assertTrue(user.is_active)

    def test_created_user_can_now_login(self):
        """Test that a created used can login after going to email link."""
        data = {
            'username': 'metsfan',
            'password1': 'potatoes',
            'password2': 'potatoes',
            'email': 'mets@woo.com'
        }
        self.client.post('/accounts/register/', data, follow=True)
        content = mail.outbox[0].message().get_payload()
        link = content.split('\n\n')[2]
        self.client.get(link)
        user = User.objects.get(username='metsfan')
        self.assertTrue(user.is_active)

        response = self.client.post(reverse_lazy('login'), {'username': 'metsfan', 'password': 'potatoes'}, follow=True)
        login_response = response.status_code
        login_response_content = response.content.decode('utf-8')
        self.assertEqual(login_response, 200)
        self.assertIn('metsfan', login_response_content)
