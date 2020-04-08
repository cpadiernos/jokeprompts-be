import json
from django.test import TestCase
from django.urls import reverse

from jokes.models import Joke
from jokes.serializers import JokeSerializer

class JokeAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Joke.objects.create(
            prompt = 'Working out.',
            text = 'Programming is 10% science, 20% ingenuity, and 70% getting the ingenuity to work with the science.'
        )
        Joke.objects.create(
            prompt = 'Bad night at the bar.',
            text = 'Eight bytes walk into a bar. The bartender asks, “Can I get you anything?” “Yeah,” reply the bytes. “Make us a double.”'
        )
    
    def test_get_returns_200_success_code(self):
        response = self.client.get(reverse('joke-list'))
        jokes = Joke.objects.all()
        serlializer = JokeSerializer(jokes, many=True)
        self.assertEqual(response.data, serlializer.data)
        self.assertEqual(response.status_code, 200)
        
    def test_get_uses_correct_serializer(self):
        response = self.client.get(reverse('joke-list'))
        jokes = Joke.objects.all()
        serlializer = JokeSerializer(jokes, many=True)
        self.assertEqual(response.data, serlializer.data)
        
    def test_get_returns_list_of_jokes(self):
        joke1 = Joke.objects.get(pk='1')
        joke2 = Joke.objects.get(pk='2')
        response = self.client.get(reverse('joke-list'))
        self.assertEqual(
            json.loads(response.content),
            [
                {'pk': joke1.pk, 'prompt': joke1.prompt, 'text': joke1.text},
                {'pk': joke2.pk, 'prompt': joke2.prompt, 'text': joke2.text},
                
            ]
        )
        
    def test_valid_joke_post_returns_201_created_code(self):
        prompt = 'Expectations vs reality.'
        text = 'There are 10 kinds of people in this world: those who know binary, those who don’t, and those who didn\'t expect this joke to be in ternary.'
        response = self.client.post(
            reverse('joke-list'),
            data=json.dumps({'prompt': prompt, 'text': text}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        
    def test_invalid_joke_post_returns_400_bad_request_code(self):
        prompt = 'Expectations vs reality.'
        response = self.client.post(
            reverse('joke-list'),
            data=json.dumps({'prompt': prompt}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        
    def test_put_non_existing_joke_returns_404_not_found_code(self):
        response = self.client.put(
            reverse('joke-detail', kwargs={'pk': '99'}),
        )
        self.assertEqual(response.status_code, 404)
        
    def test_delete_non_existing_joke_returns_404_not_found_code(self):
        response = self.client.delete(
            reverse('joke-detail', kwargs={'pk': '99'}),
        )
        self.assertEqual(response.status_code, 404)
        
    def test_valid_put_joke_returns_204_no_content_code(self):
        joke = Joke.objects.get(pk='1')
        response = self.client.put(
            reverse('joke-detail', kwargs={'pk': '1'}),
            {'prompt': 'other prompt', 'text': 'other text'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 204)
        
    def test_invalid_put_joke_returns_400_bad_request_code(self):
        joke = Joke.objects.get(pk='1')
        response = self.client.put(
            reverse('joke-detail', kwargs={'pk': '1'}),
             data=json.dumps({'prompt': '', 'text': 'other text'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        
    def test_valid_delete_joke_returns_204_no_content_code(self):
        response = self.client.delete(
            reverse('joke-detail', kwargs={'pk': '1'}),
        )
        self.assertEqual(response.status_code, 204)