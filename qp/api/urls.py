from django.urls import path, re_path
from knox import views as knox_views

from qp.api.views import (
    qpPingView
)

from qp.api.views.player import (
    qpRegisterView,
    qpLoginView
)

urlpatterns = [
    re_path("", qpPingView.as_view()),
    re_path("^register/", qpRegisterView.as_view()),
    re_path("^login/", qpLoginView.as_view()),
    re_path("^logout/", knox_views.LogoutAllView.as_view(), name="knox_logoutall")
]
