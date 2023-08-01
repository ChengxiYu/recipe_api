from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest(TestCase):

    def test_create_user_with_email_successful(self):
        email = "yuchengxi123@gmail.com"
        password = "yuchengxi123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        test_cases = [
            ['test1@Example.com', 'test1@example.com'],
            ['TesT2@EXAMPLE.COM', 'TesT2@example.com'],
            ['test3@example.COM', 'test3@example.com'],
            ['Test4@examPle.Com', 'Test4@example.com']
        ]
        for email, expected in test_cases:
            user = get_user_model().objects.create_user(email, 'yuchengxi123')
            self.assertEqual(expected, user.email)

    def test_new_user_no_email_raise_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'yuchengxi123')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'yuchengxi123@gmail.com', 'yuchengxi123'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
