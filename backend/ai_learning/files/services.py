from django.core.files.uploadedfile import TemporaryUploadedFile

from files.models import TemporaryFile


def temporary_file_create(file: TemporaryUploadedFile) -> TemporaryFile:
    file_obj = TemporaryFile.objects.create(
        file=file,
        name=file.name
    )

    return file_obj
