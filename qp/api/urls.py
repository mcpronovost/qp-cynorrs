from django.urls import path, re_path
from knox import views as knox_views

from qp.api.views import (
    qpPingView
)

from qp.api.views.game import (
    qpGameActionTravelView
)

from qp.api.views.player import (
    qpPlayerMeRetrieveView,
    qpPlayerMeCharactersHerosListView,
    qpPlayerMeCharactersRetrieveView,
    qpPlayerMeHerosListView,
    qpPlayerMeWorldsListView,
    qpPlayerMeWorldRetrieveView,
    qpPlayerMeWorldForumRetrieveView
)

from qp.api.views.forum import (
    qpForumRetrieveView,
    qpForumZoneRetrieveView,
    qpForumTerritoryRetrieveView,
    qpForumSectorRetrieveView,
    qpForumChapterRetrieveView,
    qpForumChapterCreateView,
    qpForumChapterMessagesListView,
    qpForumChapterMessageCreateView,
    qpForumChapterMessageEditView
)

from qp.api.views.user import (
    qpRegisterView,
    qpLoginView
)

from qp.api.views.world import (
    qpWorldsListView,
    qpWorldsRetrieveAPIView
)

urlpatterns = [
    path("", qpPingView.as_view()),

    path("me/", qpPlayerMeRetrieveView.as_view()),
    path("me/characters/heros/", qpPlayerMeCharactersHerosListView.as_view()),
    path("me/characters/<int:pk>/", qpPlayerMeCharactersRetrieveView.as_view()),
    path("me/heros/", qpPlayerMeHerosListView.as_view()),
    path("me/worlds/", qpPlayerMeWorldsListView.as_view()),
    path("me/worlds/<int:pk>/", qpPlayerMeWorldRetrieveView.as_view()),
    path("me/forums/<int:pk>/", qpPlayerMeWorldForumRetrieveView.as_view()),

    path("game/action/travel/", qpGameActionTravelView.as_view()),

    path("worlds/", qpWorldsListView.as_view()),
    path("worlds/<slug:slug>/", qpWorldsRetrieveAPIView.as_view()),
    path("worlds/forums/<int:pk>/", qpForumRetrieveView.as_view()),
    path("worlds/zones/<int:pk>/", qpForumZoneRetrieveView.as_view()),
    path("worlds/territories/<int:pk>/", qpForumTerritoryRetrieveView.as_view()),
    path("worlds/territories/<int:pk>/chapters/create/", qpForumChapterCreateView.as_view()),
    path("worlds/sectors/<int:pk>/", qpForumSectorRetrieveView.as_view()),
    path("worlds/sectors/<int:pk>/chapters/create/", qpForumChapterCreateView.as_view()),
    path("worlds/chapters/<int:pk>/", qpForumChapterRetrieveView.as_view()),
    path("worlds/chapters/<int:pk>/messages/", qpForumChapterMessagesListView.as_view()),
    path("worlds/chapters/<int:pk>/messages/create/", qpForumChapterMessageCreateView.as_view()),
    path("worlds/messages/<int:pk>/edit/", qpForumChapterMessageEditView.as_view()),
    path("worlds/messages/<int:pk>/delete/", qpForumChapterMessageEditView.as_view()),

    path("register/", qpRegisterView.as_view(), name="auth_register"),
    path("login/", qpLoginView.as_view()),
    path("logout/", knox_views.LogoutAllView.as_view(), name="knox_logoutall")
]
