from django.test import TestCase
from django.contrib.auth import get_user_model


class UserRegisterTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email="test@example.com", password="test123", name="Test")

    def test_no_repeated_account(self):
        form_data = {"email": "test@example.com", "password": "test123", "name": "Test23"}

        response = self.client.post("/accounts/register/", form_data)

        self.assertEqual(response.status_code, 400)

    def test_new_account(self):
        form_data = {"email": "New@example.com", "password": "test123", "name": "Test23"}

        response = self.client.post("/accounts/register/", form_data)

        self.assertEqual(response.status_code, 302)

    def test_no_name_form(self):
        form_data = {"email": "New@example.com", "password": "test123"}

        response = self.client.post("/accounts/register/", form_data)

        self.assertEqual(response.status_code, 400)


class UserLoginTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email="test@example.com", password="test123", name="Test")

    def test_post_valid_form_User_not_verified(self):
        form_data = {"email": "test@example.com", "password": "test123"}

        response = self.client.post("/accounts/login/", form_data)

        self.assertEqual(response.status_code, 404)

    def test_post_invalid_password_form(self):
        form_data = {"email": "test@example.com", "password": "wrong"}

        response = self.client.post("/accounts/login/", form_data)

        self.assertEqual(response.status_code, 404)

    def test_post_invalid_email_form(self):
        form_data = {"email": "testasdas@example.com", "password": "wrong"}

        response = self.client.post("/accounts/login/", form_data)

        self.assertEqual(response.status_code, 403)

    def test_post_verified_user(self):
        self.user.is_active = True
        self.user.save()

        form_data = {"email": "test@example.com", "password": "test123"}

        response = self.client.post("/accounts/login/", form_data)

        self.assertRedirects(response, "/")
