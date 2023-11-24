from django.contrib.auth.models import AbstractUser

from rest_framework.request import Request


class DefaultField:
    requires_context = True

    def bind(self, serializer):
        self.serializer = serializer

    def __call__(self, serializer):
        self.bind(serializer)

    @property
    def request(self) -> Request:
        return self.serializer.context["request"]

    @property
    def user(self) -> AbstractUser:
        return self.request.user
