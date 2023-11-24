from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
)

from .models import Dosage, DosageUsage, Prescription
from .serializers import DosageSerializer, DosageUsageSerializer, PrescriptionSerializer


class DosageViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    queryset = Dosage.objects.all()
    serializer_class = DosageSerializer


class DosageUsageViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    queryset = DosageUsage.objects.all()
    serializer_class = DosageUsageSerializer()


class PrescriptionViewSet(ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
