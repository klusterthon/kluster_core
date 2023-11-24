from django.urls import path, include

from account.routes import account_route
from tracker.routes import tracker_route
from inventory.routes import inventory_route

urlpatterns = [
    path(r"account/", include(account_route.urls)),
    path(r"tracker/", include(tracker_route.urls)),
    path(r"inventory/", include(inventory_route.urls)),
]
