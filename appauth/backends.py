from django.contrib.auth.hashers import check_password
from .models import AppUser, EMAIL_REGEX, PHONE_REGEX


SESSION_KEY = '_auth_user_id'
BACKEND_SESSION_KEY = '_auth_user_backend'
HASH_SESSION_KEY = '_auth_user_hash'
REDIRECT_FIELD_NAME = 'next'


class AppAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            if EMAIL_REGEX.match(username):
                username = username.lower()
                user = AppUser.objects.get(email=username)
            elif PHONE_REGEX.match(username):
                user = AppUser.objects.get(phone_number=username)
            else:
                user = AppUser.objects.get(username=username)
        except AppUser.DoesNotExist:
            return None

        if check_password(password, user.password):
            # Authentication success by returning the user
            return user
        else:
            # Authentication fails if None is returned
            return None

    def get_user(self, user_id):
        try:
            user = AppUser.objects.get(id=user_id)
            return user
        except AppUser.DoesNotExist:
            return None
