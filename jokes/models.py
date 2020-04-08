from django.db import models

class Joke(models.Model):
    prompt = models.TextField()
    text = models.TextField()
    
    def __str__(self):
        return self.text
