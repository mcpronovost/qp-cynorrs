from django.contrib import admin
from django.urls import re_path
from django.views.generic import TemplateView

from qp.views import app

urlpatterns = [
    re_path("admin/", admin.site.urls),
    re_path("^", app)
]
