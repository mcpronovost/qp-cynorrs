
from django.db.models import Q

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from qp.forum.models import (
    qpForum
)

from qp.api.serializers.forum import (
    qpForumSerializer
)

class qpForumRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpForumSerializer
    queryset = qpForum.objects.all()
    lookup_field = "pk"
