from django.urls import path
from .views import VendorDashBoard
app_name = "vendor"

urlpatterns = [
    path("", view=VendorDashBoard.as_view(),)
]
