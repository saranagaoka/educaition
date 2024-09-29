import base64
import requests
from django.conf import settings


def image_to_text(file_path: str):
    """Read text from image"""
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    r = requests.post(
        f'{settings.AI_BACKEND_HOSTNAME}/note_to_text',
        json={
            'image': encoded_string.decode('utf-8'),
        },
        headers={
            'Content-Type': 'application/json',
        }
    )

    print(r.status_code)
    print(r.text)

    return r.text


def text_to_quiz(text: str):
    """Generate quiz questions from text"""
    r = requests.post(
        f'{settings.AI_BACKEND_HOSTNAME}/create_questions_abc',
        json={
            'note_content': text,
        },
        headers={
            'Content-Type': 'application/json',
        }
    )

    print(r.status_code)
    print(r.text)

    return r.json()


def text_to_open_question(text: str):
    """Generate open questions from text"""
    r = requests.post(
        f'{settings.AI_BACKEND_HOSTNAME}/create_questions_open',
        json={
            'note_content': text,
        },
        headers={
            'Content-Type': 'application/json',
        }
    )

    print(r.status_code)
    print(r.text)

    return r.json()


def enrich_text(text: str):
    """Generate enriched text from note"""
    r = requests.post(
        f'{settings.AI_BACKEND_HOSTNAME}/create_podcast_text',
        json={
            'note_content': text,
        },
        headers={
            'Content-Type': 'application/json',
        }
    )

    print(r.status_code)
    print(r.text)

    return r.text


def text_to_topic(text: str):
    """Generate topic from text"""
    r = requests.post(
        f'{settings.AI_BACKEND_HOSTNAME}/create_title',
        json={
            'note_content': text,
        },
        headers={
            'Content-Type': 'application/json',
        }
    )

    print(r.status_code)
    print(r.text)

    return r.text


def text_to_audio(text: str):
    """Generate audio from enriched text"""
    r = requests.post(
        f'{settings.AI_BACKEND_HOSTNAME}/create_podcast',
        json={
            'note_content': text,
        },
        headers={
            'Content-Type': 'application/json',
        }
    )

    print(r.status_code)
    print(r.text)

    return r.json()

