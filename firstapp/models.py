# firstapp/models.py
from django.db import models
from django.conf import settings

class VocabItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vocab_items')
    gender = models.CharField(max_length=10, blank=True)
    word = models.CharField(max_length=100)
    english_meaning = models.CharField(max_length=200)
    part_of_speech = models.CharField(max_length=50, blank=True)
    other_comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.word} ({self.english_meaning})"