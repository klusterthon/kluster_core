from rest_framework import serializers

from .models import User, Personnel, Patient, Allergy 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("password",)
        model = User 
        
class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("user",)
        model = Personnel

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ()
        model = Allergy

class PatientSerializer(serializers.ModelSerializer):
    allergies = AllergySerializer(many=True)
    
    class Meta:
        exclude = ("user",)
        model = Patient
        