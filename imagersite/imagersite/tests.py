from django.test import TestCase, Client
from django.core import mail
from urllib.parse import urlparse


class BasicViewTests(TestCase):
    '''
    Class for testing views
    '''
    def test_home(self):
        '''
        Test home route
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'generic/home.html')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_login(self):
        '''
        Test login route
        '''
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/login.html')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_register(self):
        '''
        Test register route
        '''
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/registration_form.html')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_logout(self):
        '''
        Test logout route
        '''
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/logout.html')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_register_user(self):
        '''
        Test for user registration
        '''
        self.client.post('/accounts/register/', {'username': 'person', 'password1': 'codefellows1', 'password2': 'codefellows1', 'email': 'email@email.com'})
        email = mail.outbox[0]
        link = email.body.splitlines()[-1]
        link = urlparse(link)
        self.client.get(link.path)
        self.assertTrue(self.client.login(username='person', password='codefellows1'))
