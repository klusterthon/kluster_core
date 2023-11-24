from rest_framework.routers import DefaultRouter

from .viewsets import DrugViewSet

inventory_route = DefaultRouter()

inventory_route.register(r"drugs", DrugViewSet)
