from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Personnel(models.Model):
    """
    The personnel model represents a health-care provider entity
    """

    class PersonnelType(models.TextChoices):
        DOCTOR = "DOCTOR", "Doctor"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    type = models.TextField(choices=PersonnelType.choices)

    def __str__(self) -> str:
        return "<%s,%s>" % self.type, self.user.get_full_name()


class Patient(models.Model):
    pass
