from pathlib import Path

import uuid
from django.contrib.auth import get_user_model
from django.db import models

from base.models import DateAwareModel

User = get_user_model()


def get_file_upload_path(instance, filename):
    random_filename = uuid.uuid4().hex
    extension = Path(filename).suffix
    dest_filename = f'{random_filename}{extension}'
    return Path('temporary_files') / dest_filename


class TemporaryFile(DateAwareModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to=get_file_upload_path)
    name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'{self.file.name}'
