from django.contrib.auth import get_user_model
from django.db.models import QuerySet, Subquery, OuterRef

from notes.models import Note, Question

User = get_user_model()


def note_list(owner: User) -> QuerySet[Note]:
    qs = Note.objects.filter(owner=owner)
    return qs


def note_get(owner: User, id: int) -> Note:
    note = Note.objects.all().get(owner=owner, id=id)
    note.next_note = Note.objects.filter(subject=note.subject).exclude(id=note.id).first()
    return note


def question_list(owner: User, note_id: int) -> QuerySet[Question]:
    qs = Question.objects.filter(note__owner=owner, note_id=note_id)
    return qs
