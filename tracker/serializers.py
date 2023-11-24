from typing import Any
from rest_framework import serializers

from kluster_core.fields import DefaultField

from account.serializers import PatientSerializer, PersonnelSerializer

from inventory.serializers import DrugSerializer

from .models import Dosage, DosageUsage, Prescription


# default fields
class PatientDefault(DefaultField):
    requires_context = True

    def __call__(self, serializer):
        self.bind(serializer)
        if hasattr(self.user, "patient"):
            return self.user.patient

        return self.request.data.get("patient")


class PersonnelDefault(DefaultField):
    requires_context = True

    def __call__(self, serializer):
        self.bind(serializer)
        if hasattr(self.user, "personnel"):
            return self.user.personnel

        return self.request.data.get("personnel")


class DosageSerializer(serializers.ModelSerializer):
    drug = DrugSerializer()

    class Meta:
        model = Dosage
        exclude = ()


class DosageUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DosageUsage
        exclude = ()


class PrescriptionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(
        default=PatientDefault(),
    )
    personnel = PersonnelSerializer(
        default=PersonnelDefault(),
    )
    dosage = DosageSerializer()

    class Meta:
        model = Prescription
        exclude = ()


serializers.CurrentUserDefault()
