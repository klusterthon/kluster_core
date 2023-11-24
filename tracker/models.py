from django.db import models
from django.utils import timezone
from django.db.models.manager import BaseManager
from django.core.validators import MinValueValidator

from account.models import Patient, Personnel

from inventory.models import Drug


class Prescription(models.Model):
    dosage: BaseManager["Dosage"]

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )

    personnel = models.ForeignKey(
        Personnel,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    intruction = models.TextField(
        null=True,
        blank=True,
    )

    note = models.TextField(
        null=True,
        blank=True,
    )


class Dosage(models.Model):
    reminders: BaseManager["Reminder"]

    class DosageForm(models.TextChoices):
        GRAM = "GRAM", "Gram"
        PILLS = "PILLS", "Pills"
        DROPS = "DROPS", "Drops"
        CAPSULE = "CAPSULE", "Capsule"
        MILIGRAM = "MILIGRAM", "Miligram"

    class Interval(models.TextChoices):
        DAILY = "DAILY", "Daily"
        CYCLIC = "CYCLIC", "Cyclic"
        WEEKLY = "WEEKLY", "Weekly"
        INTERVAL = "INTERVAL", "Interval"
        SPECIFIC = "SPECIFIC", "Specific"

    prescription = models.OneToOneField(
        Prescription,
        on_delete=models.CASCADE,
    )

    drug = models.ForeignKey(
        Drug,
        on_delete=models.CASCADE,
    )

    count = models.IntegerField(
        validators=[
            MinValueValidator(1),
        ],
    )

    form = models.FloatField(
        choices=DosageForm.choices,
        help_text="what form is the medicine?",
    )

    quantity = models.FloatField(
        help_text="Choose the medication strength",
    )

    interval = models.TextField(
        choices=Interval.choices, help_text="How do you take this medication?"
    )

    start_date = models.DateTimeField(
        help_text="Set treatment duration",
    )

    end_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Calculate end date from input (How long are you taking the medicine?)",
    )

    @property
    def is_infinite_dosage(self):
        return self.end_date is None

    @property
    def is_dosage_complete(self):
        if not self.is_infinite_dosage:
            return self.end_date > timezone.now()

        return False

    @property
    def has_reminder(self):
        return self.reminders is not None and self.reminders.exists()


class Reminder(models.Model):
    dosage = models.ForeignKey(
        Dosage,
        on_delete=models.CASCADE,
        related_name="reminders",
    )

    pill_count = models.IntegerField(
        null=True,
        blank=True,
        help_text="Number of pill(s)",
        validators=[
            MinValueValidator(1),
        ],
    )


class DosageUsage(models.Model):
    class Status(models.TextChoices):
        TAKEN = "TAKEN", "Taken"
        PENDING = "PENDING", "PENDING"
        OVERDUE = "OVERDUE", "Overdue"

    dosage = models.ForeignKey(
        Dosage,
        on_delete=models.CASCADE,
    )
    time = models.DateTimeField(
        help_text="Time and date taken",
    )
    status = models.TextField(choices=Status.choices)
