from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        response = self.client.post(
            reverse('signup'), {
                'username': 'testuser',
                'email': 'testuser@gmail.com',
                'password1': 'fJ7rM8ivT8fKD',
                'password2': 'fJ7rM8ivT8fKD',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')
        self.assertEqual(get_user_model().objects.all()[0].email, 'testuser@gmail.com')