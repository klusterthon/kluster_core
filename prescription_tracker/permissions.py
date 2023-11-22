from typing import Iterable, List, Optional, TypedDict

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


class MethodPermissonType(TypedDict):
    ["GET", "POST", "PATCH", "DELETE"]: BasePermission | Iterable[BasePermission]

def ViewMethodPermissionBuilder(permission_dict: MethodPermissonType):
	class PermissionClass(BasePermission):
		def _get_permissions(self, method: str) -> Optional[List[BasePermission]]:
			match_keys = []

			for key in dict.keys(permission_dict):
				if isinstance(key, (list, tuple)) and method in key:
					match_keys.append(key)
				
				if isinstance(key, str):
					match_keys.append(key)
						
				for key in match_keys:
					match_keys.extend([permission  for permission in permission_dict[key]])
						
				return match_keys

		def has_permission(self, request: Request, view: APIView):
			permissions = self._get_permissions(request)
			for permission in permissions:
				if isinstance(permission, (list, tuple)):
					result = True 

					for permission_class in permission:
						return result and permission_class().has_object_permission(request, view)

				return permission().has_object_permission(request, view)

			return False
				
		def has_object_permission(self, request, view, obj):
			return super().has_object_permission(request, view, obj)
				

	return PermissionClass
