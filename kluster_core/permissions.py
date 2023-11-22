from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.permissions import BasePermission


class MedicalPersonnelOnly(BasePermission):
    def has_permission(self, request: Request, view: APIView):
        return hasattr(request.user, "personnel")

    def has_object_permission(self, request: Request, view: APIView, instance: any):
        return True


class PatientOnly(BasePermission):
    def has_permission(self, request: Request, view: APIView):
        return hasattr(request.user, "patient")

    def has_object_permission(self, request: Request, view: APIView, instance: any):
        return True
