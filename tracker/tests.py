from django.test import TestCase

from rest_framework.permissions import AllowAny

from .permissions import ViewMethodPermissionBuilder


class ViewMethodPermissionTest(TestCase):
    def test_single_permission_for_single_method(self):
        permission_class = ViewMethodPermissionBuilder({"GET": AllowAny})
        print(permission_class.has_permission())
        

    def test_multiple_permission_for_single_methods(self):
        pass

    def test_single_permission_for_multiple_method(self):
        pass

    def test_multiple_permission_for_multiple_methods(self):
        pass
