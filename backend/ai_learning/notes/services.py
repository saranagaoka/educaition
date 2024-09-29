from threading import Thread
from typing import List

from django.contrib.auth import get_user_model

from files.helpers import to_file
from files.models import TemporaryFile
from integrations.utils import image_to_text, text_to_quiz, enrich_text, text_to_open_question, text_to_topic, \
    text_to_audio
from notes.models import Note, Question, Answer

User = get_user_model()


def note_create(owner: User, subject: str, temp_file_uuids: List[str]) -> Note:
    note = Note.objects.create(owner=owner, text='', subject=subject)

    thread = Thread(
        target=process_note,
        kwargs={
            'note': note,
            'temp_file_uuids': temp_file_uuids
        }
    )
    thread.start()

    return note


def note_update(note_id: int, is_read=None, is_listened=None, is_quiz_done=None) -> Note:
    note = Note.objects.get(id=note_id)

    if is_read is not None:
        note.is_read = is_read
    if is_listened is not None:
        note.is_listened = is_listened
    if is_quiz_done is not None:
        note.is_quiz_done = is_quiz_done

    note.save()

    return note


def process_note(note: Note, temp_file_uuids: List[str]):
    joined_text = ''
    for temp_file_uuid in temp_file_uuids:
        temp_file = TemporaryFile.objects.get(uuid=temp_file_uuid)
        text = image_to_text(temp_file.file.path)
        joined_text = '\n'.join([joined_text, text])

    note.text = joined_text
    note.save()

    # enriched_text = enrich_text(note.text)
    # note.enriched_text = enriched_text
    # note.save()

    closed_questions = text_to_quiz(note.text)
    for question_details in closed_questions:
        question = Question.objects.create(
            type=Question.Type.CLOSED,
            text=question_details['pytanie'],
            note=note
        )

        for i, answer_text in enumerate(question_details['odpowiedzi']):
            answer = Answer.objects.create(
                text=answer_text,
                question=question,
                correct=i == question_details['prawidlowa_odpowiedz'],
            )

    # open_questions = text_to_open_question(note.text)
    # for question_details in open_questions:
    #     question = Question.objects.create(
    #         type=Question.Type.OPEN,
    #         text=question_details['pytanie'],
    #         note=note
    #     )
    #     answer = Answer.objects.create(
    #         text=question_details['odpowiedz'],
    #         question=question,
    #         correct=True
    #     )

    topic = text_to_topic(note.text)
    topic = topic.strip('"')
    note.topic = topic
    note.save()

    audio_data = text_to_audio(note.text)
    note.enriched_text = audio_data['text']
    audio_base64 = audio_data['audio']
    in_memory_file = to_file('data:audio/mp3;base64,' + audio_base64)
    note.audio_file = in_memory_file

    note.is_ready = True
    note.save()
