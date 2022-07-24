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

from qp.api.views.forum import (
    qpForumRetrieveAPIView,
    qpForumZoneRetrieveAPIView,
    qpForumTerritoryRetrieveAPIView,
    qpForumSectorRetrieveAPIView,
    qpForumChapterRetrieveAPIView,
    qpForumChapterMessagesListAPIView,
    qpForumChapterMessageCreateAPIView,
    qpForumChapterCreateAPIView
)

from qp.api.views.world import (
    qpWorldsListView,
    qpWorldsCreateView,
    qpWorldsRetrieveAPIView
)

urlpatterns = [
    path("", qpPingView.as_view()),

    path("me/", qpPlayerView.as_view()),
    path("me/heros/", qpPlayerHerosView.as_view()),
    path("me/heros/<int:pk>/", qpPlayerHeroView.as_view()),
    path("me/worlds/create/", qpWorldsCreateView.as_view()),

    path("game/action/travel/", qpGameActionTravelView.as_view()),

    path("worlds/", qpWorldsListView.as_view()),
    path("worlds/<slug:slug>/", qpWorldsRetrieveAPIView.as_view()),
    path("worlds/forums/<int:pk>/", qpForumRetrieveAPIView.as_view()),
    path("worlds/zones/<int:pk>/", qpForumZoneRetrieveAPIView.as_view()),
    path("worlds/territories/<int:pk>/", qpForumTerritoryRetrieveAPIView.as_view()),
    path("worlds/territories/<int:pk>/chapters/create/", qpForumChapterCreateAPIView.as_view()),
    path("worlds/sectors/<int:pk>/", qpForumSectorRetrieveAPIView.as_view()),
    path("worlds/sectors/<int:pk>/chapters/create/", qpForumChapterCreateAPIView.as_view()),
    path("worlds/chapters/<int:pk>/", qpForumChapterRetrieveAPIView.as_view()),
    path("worlds/chapters/<int:pk>/messages/", qpForumChapterMessagesListAPIView.as_view()),
    path("worlds/chapters/<int:pk>/messages/create/", qpForumChapterMessageCreateAPIView.as_view()),

    path("register/", qpRegisterView.as_view(), name="auth_register"),
    path("login/", qpLoginView.as_view()),
    path("logout/", knox_views.LogoutAllView.as_view(), name="knox_logoutall")
]
