import os
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from qp.settings import FRONTEND_ROOT, MEDIA_ROOT, MEDIA_URL

from qp.views import app

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^api-auth/", include("rest_framework.urls")),
    re_path(r"^api/auth/", include("knox.urls")),
    re_path(r"^api/", include("qp.api.urls")),

    re_path(r"^media/(?P<path>.*)", serve, {"document_root": os.path.join(MEDIA_ROOT)}),
    re_path(r"^icons/(?P<path>.*)$", serve, {"document_root": os.path.join(FRONTEND_ROOT, "icons")}),
    re_path(r"^img/(?P<path>.*)$", serve, {"document_root": os.path.join(FRONTEND_ROOT, "img")}),
    re_path(r"^js/(?P<path>.*)$", serve, {"document_root": os.path.join(FRONTEND_ROOT, "js")}),
    re_path(r"^css/(?P<path>.*)$", serve, {"document_root": os.path.join(FRONTEND_ROOT, "css")}),
    re_path(r"^fonts/(?P<path>.*)$", serve, {"document_root": os.path.join(FRONTEND_ROOT, "fonts")}),

    re_path(r"^", app)
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
