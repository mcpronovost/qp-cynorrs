from django.core.exceptions import BadRequest

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from qp.player.models import (
    qpPlayer
)

from qp.api.serializers.player import (
    qpPlayerMeSerializer
)


class qpPlayerRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeSerializer
    queryset = qpPlayer.objects.all()
    lookup_field = "pk"

    def get_object(self):
        try:
            return self.request.user.player
        except Exception as e:
            print("Error on qpPlayerRetrieveView : ", e)
        return None
