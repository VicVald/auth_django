from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class AuthTests(TestCase):
    def test_register_success(self):
        response = self.client.post(reverse('authentication:register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        })
        self.assertContains(response, "Usuário registrado com sucesso!")
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_existing_email(self):
        User.objects.create_user(username='user1', email='test@example.com', password='pass')
        response = self.client.post(reverse('authentication:register'), {
            'username': 'user2',
            'email': 'test@example.com',
            'password': 'pass'
        })
        self.assertContains(response, "Email em uso, tente outro.")

    def test_register_existing_username(self):
        User.objects.create_user(username='user1', email='email1@example.com', password='pass')
        response = self.client.post(reverse('authentication:register'), {
            'username': 'user1',
            'email': 'email2@example.com',
            'password': 'pass'
        })
        self.assertContains(response, "Nome de usuário em uso, tente outro.")

    def test_login_success(self):
        self.client.post(reverse('authentication:register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        })

        response = self.client.post(reverse('authentication:login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home_page'))

