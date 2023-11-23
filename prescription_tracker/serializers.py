from rest_framework import serializers

from .models import Dosage, Prescription 


class DosageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dosage
        exclude = ()
        
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        exclude = ()
        