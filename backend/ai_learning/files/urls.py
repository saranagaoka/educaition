from django.urls import path

from files.apis import TemporaryFileUploadApi

urlpatterns = [
    path('file/upload/', TemporaryFileUploadApi.as_view(), name='upload'),
]
