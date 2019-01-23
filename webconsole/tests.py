from django.test import TestCase
import django
import logging

logging = logging.getLogger('cloud')


# Create your tests here.

print(django.get_version())

logging.debug("123")
