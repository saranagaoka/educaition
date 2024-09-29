import json

from django.http import HttpRequest
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from files.helpers import to_file
from files.services import temporary_file_create
from integrations.utils import image_to_text


class TemporaryFileUploadApi(APIView):
    class OutputSerializer(serializers.Serializer):
        uuid = serializers.UUIDField()

    def options(self, request, *args, **kwargs):
        if self.metadata_class is None:
            return self.http_method_not_allowed(request, *args, **kwargs)
        data = self.metadata_class().determine_metadata(request, self)
        return Response(data, status=status.HTTP_200_OK, headers={
            'Access-Control-Allow-Origin': '*',
        })

    def post(self, request: HttpRequest) -> Response:
        in_memory_file = request.FILES['file']

        file = temporary_file_create(file=in_memory_file)

        data = self.OutputSerializer(file, many=False).data
        return Response(data, headers={
            'Access-Control-Allow-Origin': '*'
        })
