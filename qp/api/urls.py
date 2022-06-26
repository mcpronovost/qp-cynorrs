from django.urls import path
from knox import views as knox_views

from qp.api.views.player import (
    qpRegisterView,
    qpLoginView
)

urlpatterns = [
    path("register/", qpRegisterView.as_view()),
    path("login/", qpLoginView.as_view()),
    path("logout/", knox_views.LogoutAllView.as_view(), name="knox_logoutall")
]
