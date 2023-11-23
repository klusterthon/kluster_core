from rest_framework.viewsets import ModelViewSet 
from rest_framework.schemas.openapi import AutoSchema

from .models import User, Personnel, Patient 
from .serializers import UserSerializer, PersonnelSerializer, PatientSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    
class PersonnelViewSet(ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer 
    
    def get_queryset(self):
        return Personnel.objects.filter(user=user)

class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer()

    def get_queryset(self):
        # todo all a clause for medical personnel 
        # to view patient data if has access to
        return Patient.objects.filter(user=user)
        
        