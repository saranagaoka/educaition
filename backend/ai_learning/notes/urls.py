from django.urls import path

from notes.apis import NoteCreateApi, NoteListApi, NoteDetailsApi, NoteQuizApi, NoteUpdateApi, \
    NoteQuizCheckApi

urlpatterns = [
    path('notes/create/', NoteCreateApi.as_view(), name='note-create'),
    path('notes/', NoteListApi.as_view(), name='note-list'),
    path('notes/<int:note_id>/', NoteDetailsApi.as_view(), name='note-details'),
    path('notes/<int:note_id>/update/', NoteUpdateApi.as_view(), name='note-update'),
    path('notes/<int:note_id>/quiz/', NoteQuizApi.as_view(), name='note-quiz'),
    path('notes/<int:note_id>/quiz/check/', NoteQuizCheckApi.as_view(), name='note-quiz-check'),
]
