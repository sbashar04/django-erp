from django.urls import path
from .views import CustomLoginView, CustomLogoutView, dashboard_view


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
