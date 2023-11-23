from rest_framework.routers import DefaultRouter 

from .viewsets import UserViewSet, PersonnelViewSet, PatientViewSet

account_route = DefaultRouter()

account_route.register("users", UserViewSet)
account_route.register("patients", PatientViewSet)
account_route.register("personnels", PersonnelViewSet)