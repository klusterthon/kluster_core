from rest_framework.routers import DefaultRouter 

from .viewsets import DosageViewSet, PrescriptionViewSet

tracker_route = DefaultRouter()

tracker_route.register("dosages", DosageViewSet)
tracker_route.register("prescriptions", PrescriptionViewSet)
