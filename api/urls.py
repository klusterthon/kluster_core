from django.urls import path, include

from account.routes import account_route
from prescription_tracker.routes import tracker_route

urlpatterns = [
    path(r"account/", include(account_route.urls)),
    path(r"tracker/", include(tracker_route.urls)),
]