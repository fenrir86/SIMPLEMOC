from django.test import TestCase
from django.core import mail
from django.test.client import Client
from django.urls import reverse


# Create your tests here.

class HomeViewTest(TestCase):
    def teste_hom_status_code(self):
        client =Client()
        response = client.get(reverse('core:home'))
        self.assertTemplateUsed(response,'home.html')