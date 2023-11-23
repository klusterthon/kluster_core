from rest_framework.viewsets import ModelViewSet 

from .models import Dosage, Prescription
from .serializers import DosageSerializer, PrescriptionSerializer

class DosageViewSet(ModelViewSet):
    queryset = Dosage.objects.all()
    serializer_class = DosageSerializer 
    
class PrescriptionViewSet(ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer 
    