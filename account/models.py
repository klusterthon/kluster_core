from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "MALE", "male"
        FEMALE = "FEMALE", "female"
        OTHERS = "OTHERS", "others"
        BISEXUAL = "BISEXUAL", "bisexual"
        TRANSGENDER = "TRANSGENDER", "transgender"
        
    dob = models.DateTimeField()
    sex = models.TextField(choices=Gender.choices)
    
    class Meta:
        pass

class Personnel(models.Model):
    """
    The personnel model represents a health-care provider entity
    """

    class PersonnelType(models.TextChoices):
        DOCTOR = "DOCTOR", "Doctor"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    type = models.TextField(choices=PersonnelType.choices)

    def __str__(self) -> str:
        return "<%s,%s>" % self.type, self.user.get_full_name()


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

# todo 
class Allergy(models.Model):
    class AllergyType(models.TextChoices):
        FOOD = "FOOD", "FOOD"
        DRUG = "DRUG", "DRUG"
        OTHERS = "OTHERS", "OTHERS"
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    type = models.TextField(choices=AllergyType.choices)
    drug = None 
    note = models.TextField()
    