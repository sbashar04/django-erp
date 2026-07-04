from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class CustomLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    pass


@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")
