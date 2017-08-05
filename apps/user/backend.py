from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib.auth import login


class UserBackend(object):
    """Custom Backend to user"""
    def authenticate(self, request, username=None, password=None):
        # try get user with the username parameter from function
        try:
            user = User.objects.get(username=username)
            # check password
            if check_password(password, user.password):
                # login user
                login(request, user)

                return user

            else:
                return None

        except User.DoesNotExist:
            return False

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
