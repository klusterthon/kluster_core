from django.db import models
from django.db.models import BaseManager
from django.utils import timezone

from account.models import Personnel, Patient


class Drug(models.Model):
    pass


class Prescription(models.Model):
    """
    prescription is a entity that describe the relationship between dosages and patient with a prescriptor
    Incase of a null prescriptor,
    patients are been warn for self-medication and ask if prescription is from a verified medical personnel
    """

    dosages: "BaseManager[Dosage]"
    dosage_throughs: "BaseManager[DosageThrough]"

    prescriptor = models.ForeignKey(
        Personnel,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )


class Dosage(models.Model):
    """
    Dosage record drug usage interval or fixed interval
    """

    dosage_usages: "BaseManager[DosageUsage]"

    class DosageType(models.TextChoices):
        FIXED = "FIXED", "Fixed"
        INTERVAL = "INTERVAL", "Interval"

    prescription = models.OneToOneField(
        Prescription,
        on_delete=models.CASCADE,
        related_name="dosages",
    )
    type = models.TextField(choices=DosageType.choices)
    drug = models.ForeignKey(
        Drug,
        on_delete=models.CASCADE,
    )
    duration = models.DurationField()


class DosageUsage(models.Model):
    """
    Record time a dosage is suppose to be taken, if dosage is adhere to or not?
    confirm dosage is taken via an in-app messaging

    # todo record suppose time dosage is to be taken, why?
    # we can take the Mean Square Root Error of the time difference when dosage to be taken - when dosage taken is confirm
    # make a prediction what time works best for patient to adhere is dosage usage in future.
    """

    dosage = models.ForeignKey(
        Dosage,
        on_delete=models.CASCADE,
    )
    time = models.TimeField(default=timezone.now)
    adhere = models.BooleanField(default=True)
    