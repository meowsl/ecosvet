from apps.api.auth.models import Role
from django import forms
from django.contrib.auth import get_user_model
from service_objects.fields import ModelField
from service_objects.services import Service

User = get_user_model()


class GetTargetUser(Service):
    """ """

    request_user = ModelField(User)
    id_user = forms.IntegerField(required=False)

    def process(self):
        request_user = self.cleaned_data["request_user"]
        if request_user.role == Role.STUDENT:
            return request_user
        elif request_user.role in (Role.EXPERT, Role.DEAN, Role.SUPEREXPERT):
            id_user = self.cleaned_data["id_user"]
            user = User.objects.get(pk=id_user)
            return user
