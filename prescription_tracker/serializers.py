from rest_framework.serializers import ModelSerializer

from .models import Drug, Dosage, DosageUsage, Prescription


class DrugSerializer(ModelSerializer):
    """
    Drug model serializer
    """
    class Meta:
        model = Drug
        fields = "__all__"

class DosageUsageSerializer(ModelSerializer):
    """
    DosageUsage model serializer
    """
    class Meta:
        model = DosageUsage

class DosageSerializer(ModelSerializer):
    """
    Dosage model serializer
    """
    usages = DosageUsageSerializer(many=True)

    class Meta:
        model = Dosage
        fields = "__all__"
        extra_kwargs = {
            "prescription": {"write_only": True},
        }

class PrescriptionSerializer(ModelSerializer):
    """
    Prescription model serializer
    """
    dosages = DosageSerializer(many=True)

    class Meta:
        model = Prescription
        fields = "__all__"
