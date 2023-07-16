
from django.test import SimpleTestCase

from app import multiplication


class MultiTests(SimpleTestCase):

    def test_multi_numbers(self):
        ans = multiplication.multi(10, 10)

        self.assertEqual(ans, 100)
