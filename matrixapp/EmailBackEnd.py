import email
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from matrixapp.models import CustomUser

class EmailBackEnd(ModelBackend):
    def authenticate(self, username=None,password=None, **kwargs):
        try:

            user = CustomUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except:
            return None
        # UserModel = get_user_model()
        # try:
        #     user = UserModel.objects.get(email=username)
        # except UserModel.DoesNotExist:
        #     return None
        # else:
        #     if user.check_password(password):
        #         return user
        # return None