from django.test import TestCase
from django.contrib.auth import get_user_model


class UserRegisterTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email="test@example.com", password="test123", name="Test")
        self.user.is_active = True
        self.user.save()

    def test_no_login_no_homepage(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')

    def test_login_homepage(self):
        form_data = {"email": "test@example.com", "password": "test123"}

        self.client.post("/accounts/login/", form_data)

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
