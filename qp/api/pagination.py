from rest_framework import pagination
from rest_framework.response import Response

class qpPagination(pagination.PageNumberPagination):
    page_size = 100

    def get_page_size(self, request):
        if request.user.is_authenticated:
            view = request.parser_context["view"]
            if hasattr(view, "pagination_limit"):
                return getattr(request.user.player, view.pagination_limit)
        return self.page_size

    def get_paginated_response(self, data):
        return Response({
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "count": self.page.paginator.count,
            "size": self.page.paginator.per_page,
            "results": data
        })
