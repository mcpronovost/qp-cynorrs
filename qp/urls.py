from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from qp.views import app

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    re_path("^api/auth/", include("knox.urls")),
    re_path("^api/", include("qp.api.urls")),
    re_path("^", app)
]
