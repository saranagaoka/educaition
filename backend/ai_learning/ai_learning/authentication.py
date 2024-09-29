from django.contrib.auth import get_user_model
from rest_framework import authentication


User = get_user_model()


class PassThroughAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            user = User.objects.get(email='kamil@example.com')
        except User.DoesNotExist:
            user = User.objects.create_user(
                email='kamil@example.com',
                password='ImeC5uekjnktoFA',
                first_name='Kamil',
                last_name='Smith',
                is_staff=False,
                is_superuser=False,
            )
        return user, None
