import json
from django.test import TestCase
from django.urls import reverse

from prompts.models import Prompt
from prompts.serializers import PromptSerializer

class PromptAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Prompt.objects.create(text='Malls')
        Prompt.objects.create(text='Party fouls')
        Prompt.objects.create(text='Cat jobs')
        
    def test_get_returns_200_success_code(self):
        response = self.client.get(reverse('prompt-random'))
        self.assertEqual(response.status_code, 200)
        
    def test_get_uses_correct_serializer(self):
        response = self.client.get(reverse('prompt-random'))
        pk = response.data['pk']
        prompt = Prompt.objects.get(pk=pk)
        serializer = PromptSerializer(prompt)
        self.assertEqual(response.data, serializer.data)
        
    def test_get_returns_random_prompt(self):
        response = self.client.get(reverse('prompt-random'))
        self.assertEqual(Prompt.objects.all().count(), 3)
        pk = response.data['pk']
        prompt = Prompt.objects.get(pk=pk)
        serializer = PromptSerializer(prompt)
        self.assertEqual(json.loads(response.content), serializer.data)