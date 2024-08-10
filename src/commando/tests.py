# from django.conf import settings
# from django.test import TestCase

# # Create your tests here.
# class NeonDBTestCase(TestCase):

#     def test_db_url(self):
#         DATABASE_URL = settings.DATABASE_URL
#         self.assertIn("neon.tech",DATABASE_URL)


import os
from django.conf import settings
from django.test import TestCase

class NeonDBTestCase(TestCase):

    def test_db_url(self):
        DATABASE_URL = settings.DATABASES['default']['HOST'] if 'HOST' in settings.DATABASES['default'] else None
        print(f"Using DATABASE_URL: {DATABASE_URL}")  # Print the DATABASE_URL
        self.assertIsNotNone(DATABASE_URL, "DATABASE_URL should not be None")
        self.assertIn("neon.tech", DATABASE_URL)
