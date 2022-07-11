from django.urls import path, re_path
from knox import views as knox_views

from qp.api.views import (
    qpPingView
)

from qp.api.views.game import (
    qpGameActionTravelView
)

from qp.api.views.player import (
    qpPlayerView,
    qpPlayerHerosView,
    qpPlayerHeroView,
    qpRegisterView,
    qpLoginView
)

from qp.api.views.world import (
    qpWorldsView,
    qpWorldView
)

urlpatterns = [
    path("", qpPingView.as_view()),

    path("me/", qpPlayerView.as_view()),
    path("me/heros/", qpPlayerHerosView.as_view()),
    path("me/heros/<int:pk>/", qpPlayerHeroView.as_view()),

    path("game/action/travel/", qpGameActionTravelView.as_view()),

    path("worlds/", qpWorldsView.as_view()),
    path("worlds/<int:pk>/", qpWorldView.as_view()),

    path("register/", qpRegisterView.as_view()),
    path("login/", qpLoginView.as_view()),
    path("logout/", knox_views.LogoutAllView.as_view(), name="knox_logoutall")
]
