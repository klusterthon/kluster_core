from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin

from .models import Drug
from .serializers import DrugSerializer


class DrugViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
