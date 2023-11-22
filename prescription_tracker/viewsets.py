from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin


from kluster_core.permissions import PatientOnly

class DrugViewSet(GenericViewSet):
    pass 

class DosageViewSet(GenericViewSet):
    pass 

class DosageUsageViewSet(GenericViewSet):
    permission_classes = (IsAuthenticated, PatientOnly)
    