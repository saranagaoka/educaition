from django.db.models import Subquery, OuterRef
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from base.utils import inline_serializer
from notes.models import Note, Question, Answer
from notes.selectors import note_list, note_get, question_list
from base.pagination import get_paginated_response, LimitOffsetPagination
from notes.services import note_create, note_update


# class SubjectListApi(APIView):
#     class Pagination(LimitOffsetPagination):
#         default_limit = 10
#
#     class OutputSerializer(serializers.Serializer):
#         name = serializers.CharField()
#         topics = inline_serializer(source='topic_set', many=True, fields={
#             'name': serializers.CharField(),
#         })
#
#     def options(self, request, *args, **kwargs):
#         if self.metadata_class is None:
#             return self.http_method_not_allowed(request, *args, **kwargs)
#         data = self.metadata_class().determine_metadata(request, self)
#         return Response(data, status=status.HTTP_200_OK, headers={
#             'Access-Control-Allow-Origin': '*'
#         })
#
#     def get(self, request) -> Response:
#         print(request.user)
#         subjects = subject_list(owner=request.user)
#
#         return get_paginated_response(
#             pagination_class=self.Pagination,
#             serializer_class=self.OutputSerializer,
#             queryset=subjects,
#             request=request,
#             view=self
#         )


class NoteCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        subject = serializers.CharField(default='Przyroda')
        uuids = serializers.ListField(child=serializers.UUIDField())

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()

    def options(self, request, *args, **kwargs):
        if self.metadata_class is None:
            return self.http_method_not_allowed(request, *args, **kwargs)
        data = self.metadata_class().determine_metadata(request, self)
        res = Response(data, status=status.HTTP_200_OK, headers={
            'Access-Control-Allow-Origin': '*',
            'Accept': '*/*',
            'Content-Type': 'application/json',
        })
        return res

    def post(self, request) -> Response:
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        note = note_create(
            owner=request.user,
            subject=serializer.validated_data['subject'],
            temp_file_uuids=serializer.validated_data['uuids']
        )

        serializer = self.OutputSerializer(note)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers={
            'Access-Control-Allow-Origin': '*'
        })


class NoteListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        subject = serializers.CharField()
        topic = serializers.CharField()
        is_read = serializers.BooleanField()
        is_listened = serializers.BooleanField()
        is_quiz_done = serializers.BooleanField()
        is_ready = serializers.BooleanField()
        first_question = serializers.CharField()
        duration = serializers.IntegerField()

    def options(self, request, *args, **kwargs):
        if self.metadata_class is None:
            return self.http_method_not_allowed(request, *args, **kwargs)
        data = self.metadata_class().determine_metadata(request, self)
        return Response(data, status=status.HTTP_200_OK, headers={
            'Access-Control-Allow-Origin': '*'
        })

    def get(self, request) -> Response:
        print(request.user)
        notes = note_list(owner=request.user)
        serializer = self.OutputSerializer(notes, many=True)
        return Response(serializer.data)


class NoteDetailsApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        subject = serializers.CharField()
        topic = serializers.CharField()
        text = serializers.CharField()
        enriched_text = serializers.CharField()
        enriched_text_sentences = serializers.ListField(child=serializers.CharField())
        is_read = serializers.BooleanField()
        is_listened = serializers.BooleanField()
        is_quiz_done = serializers.BooleanField()
        is_ready = serializers.BooleanField()
        audio_file = serializers.URLField()
        audio_file_absolute = serializers.URLField()
        first_question = serializers.CharField()
        next_note = inline_serializer(fields={
            'id': serializers.IntegerField(),
            'subject': serializers.CharField(),
            'topic': serializers.CharField(),
            'text': serializers.CharField(),
            'duration': serializers.IntegerField(),
            'first_question': serializers.CharField(),
        })

    def options(self, request, *args, **kwargs):
        if self.metadata_class is None:
            return self.http_method_not_allowed(request, *args, **kwargs)
        data = self.metadata_class().determine_metadata(request, self)
        return Response(data, status=status.HTTP_200_OK, headers={
            'Access-Control-Allow-Origin': '*'
        })

    def get(self, request, note_id) -> Response:
        note = note_get(owner=request.user, id=note_id)
        serializer = self.OutputSerializer(note)
        return Response(serializer.data, headers={
            'Access-Control-Allow-Origin': '*'
        })


class NoteUpdateApi(APIView):
    class InputSerializer(serializers.Serializer):
        is_read = serializers.BooleanField(required=False, default=None)
        is_listened = serializers.BooleanField(required=False, default=None)
        is_quiz_done = serializers.BooleanField(required=False, default=None)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        subject = serializers.CharField()
        topic = serializers.CharField()
        text = serializers.CharField()
        enriched_text = serializers.CharField()
        enriched_text_sentences = serializers.ListField(child=serializers.CharField())
        is_read = serializers.BooleanField()
        is_listened = serializers.BooleanField()
        is_quiz_done = serializers.BooleanField()
        is_ready = serializers.BooleanField()

    def options(self, request, *args, **kwargs):
        if self.metadata_class is None:
            return self.http_method_not_allowed(request, *args, **kwargs)
        data = self.metadata_class().determine_metadata(request, self)
        return Response(data, status=status.HTTP_200_OK, headers={
            'Access-Control-Allow-Origin': '*'
        })

    def patch(self, request, note_id) -> Response:
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        note = note_update(note_id, **serializer.validated_data)

        serializer = self.OutputSerializer(note)
        return Response(serializer.data, headers={
            'Access-Control-Allow-Origin': '*'
        })


class NoteQuizApi(APIView):
    class OutputSerializer(serializers.Serializer):
        questions = inline_serializer(many=True, fields={
            'id': serializers.IntegerField(),
            'text': serializers.CharField(),
            'type': serializers.CharField(),
            'answers': inline_serializer(source='answer_set', many=True, fields={
                'id': serializers.IntegerField(),
                'text': serializers.CharField(),
                'correct': serializers.BooleanField(),
            })
        })
        subject = serializers.CharField()
        topic = serializers.CharField()
        is_read = serializers.BooleanField()
        is_listened = serializers.BooleanField()
        is_quiz_done = serializers.BooleanField()
        is_ready = serializers.BooleanField()
        next_note = inline_serializer(fields={
            'id': serializers.IntegerField(),
            'subject': serializers.CharField(),
            'topic': serializers.CharField(),
            'text': serializers.CharField(),
            'duration': serializers.IntegerField(),
            'first_question': serializers.CharField(),
        })

    def options(self, request, *args, **kwargs):
        if self.metadata_class is None:
            return self.http_method_not_allowed(request, *args, **kwargs)
        data = self.metadata_class().determine_metadata(request, self)
        return Response(data, status=status.HTTP_200_OK, headers={
            'Access-Control-Allow-Origin': '*'
        })

    def get(self, request, note_id) -> Response:
        note = note_get(owner=request.user, id=note_id)
        questions = question_list(owner=request.user, note_id=note_id)
        serializer = self.OutputSerializer({
            'topic': note.topic,
            'subject': note.subject,
            'questions': questions,
            'is_read': note.is_read,
            'is_listened': note.is_listened,
            'is_quiz_done': note.is_quiz_done,
            'is_ready': note.is_ready,
            'next_note': note.next_note
        })
        return Response(serializer.data, headers={
            'Access-Control-Allow-Origin': '*'
        })


class NoteQuizCheckApi(APIView):
    class InputSerializer(serializers.Serializer):
        answers = inline_serializer(many=True, fields={
            'question_id': serializers.IntegerField(),
            'answer_id': serializers.IntegerField(required=False),
            'answer_text': serializers.CharField(required=False),
        })

        def clean_answers(self, data):
            for details in data:
                if not details['answer_id'] and not details['answer_text']:
                    raise ValidationError(f"Question {details['question_id']} did not get any answer.")

    class OutputSerializer(serializers.Serializer):
        answers = inline_serializer(many=True, fields={
            'question_id': serializers.IntegerField(),
            'correct': serializers.BooleanField(),
        })

    def options(self, request, *args, **kwargs):
        if self.metadata_class is None:
            return self.http_method_not_allowed(request, *args, **kwargs)
        data = self.metadata_class().determine_metadata(request, self)
        return Response(data, status=status.HTTP_200_OK, headers={
            'Access-Control-Allow-Origin': '*'
        })

    def post(self, request, note_id: int) -> Response:
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        note = Note.objects.get(id=note_id)
        questions_with_answers = dict(
            note.question_set.filter(
                type=Question.Type.CLOSED
            ).annotate(
                correct_answer=Subquery(
                    Answer.objects.filter(question_id=OuterRef('id'), correct=True).values_list('id', flat=True))
            ).values_list(
                'id', 'correct_answer'
            )
        )

        data = [
            {
                'question_id': details.get('question_id'),
                'correct': details.get('answer_id') == questions_with_answers[details.get('question_id')]
            }
            for details in serializer.validated_data['answers']
        ]

        serializer = self.OutputSerializer({'answers': data})
        return Response(serializer.data, headers={
            'Access-Control-Allow-Origin': '*'
        })
