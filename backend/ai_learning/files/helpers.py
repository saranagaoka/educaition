import base64
import io
import sys

from django.core.exceptions import SuspiciousOperation
from django.core.files.uploadedfile import InMemoryUploadedFile


def to_file(img_base64: str):
    # 'data:image/png;base64,<base64 encoded string>'
    try:
        idx = img_base64[:50].find(',')  # comma should be pretty early on

        if not idx or not img_base64.startswith('data:'):
            raise Exception('base64 image does not contain valid base64')

        base64file = img_base64[idx+1:]
        attributes = img_base64[:idx]
        content_type = attributes[len('data:'):attributes.find(';')]
        file_type = content_type.split('/')[-1]
    except Exception as e:
        print(str(e))
        raise SuspiciousOperation("Invalid picture")

    f = io.BytesIO(base64.b64decode(base64file))
    image = InMemoryUploadedFile(
        f,
        field_name='temp_file',
        name=f'temp_file.{file_type}',  # use UUIDv4 or something
        content_type=content_type,
        size=sys.getsizeof(f),
        charset=None
    )
    return image
