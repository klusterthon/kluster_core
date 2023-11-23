from django.contrib import admin
from django.urls import path, include

from rest_framework.permissions import AllowAny

from drf_yasg import openapi 
from drf_yasg.views import get_schema_view
 
SchemaView = get_schema_view( 
     openapi.Info( 
         title="Kluster", 
         default_version="v1", 
         description="", 
         terms_of_service="", 
         contact=openapi.Contact(email=""), 
         license=openapi.License(name="MIT License"), 
     ), 
     public=True, 
     permission_classes=[AllowAny], 
)
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(r'', SchemaView.with_ui("swagger", cache_timeout=0)),
]
