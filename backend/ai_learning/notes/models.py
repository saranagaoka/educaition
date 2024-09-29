import re
import uuid
from pathlib import Path

from django.contrib.auth import get_user_model
from django.db import models
from base.models import DateAwareModel

User = get_user_model()


def get_file_upload_path(instance, filename):
    random_filename = uuid.uuid4().hex
    extension = Path(filename).suffix
    dest_filename = f'{random_filename}{extension}'
    return Path('notes') / dest_filename


class Note(DateAwareModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    text = models.TextField()
    enriched_text = models.TextField()
    audio_file = models.FileField(upload_to=get_file_upload_path, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    is_listened = models.BooleanField(default=False)
    is_quiz_done = models.BooleanField(default=False)
    is_ready = models.BooleanField(default=False, help_text='Is note fully processed')

    def __str__(self):
        return f'{self.topic} - {self.text[:100]}'

    @property
    def enriched_text_sentences(self):
        sentences = re.split(r'\n|\. ', self.enriched_text)
        sentences = [sentence for sentence in sentences if sentence]
        return sentences

    @property
    def duration(self):
        return round(len(self.enriched_text) / 1000)

    @property
    def audio_file_absolute(self):
        if not self.audio_file:
            return ''
        return self.audio_file.url

    @property
    def first_question(self):
        question = self.question_set.first()
        if not question:
            return None
        return question.text


class Question(DateAwareModel):
    class Type(models.TextChoices):
        OPEN = 'open'
        CLOSED = 'closed'

    type = models.CharField(max_length=32, choices=Type.choices)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.note} - {self.text[:100]}'


class Answer(DateAwareModel):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question} - {self.text[:100]}'
