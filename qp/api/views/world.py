from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from qp.world.models import qpWorld


class qpWorldsView(APIView):

    def get(self, request):
        worlds_data = [
            {
                "id": 0,
                "name": "Sagars",
                "zones": [
                    {
                        "id": 1,
                        "name": "Zone A",
                        "territories": [
                            {
                                "id": 2,
                                "name": "Territoire A-1",
                                "sectors": [
                                    {
                                        "id": 4,
                                        "name": "Secteur A-1-A"
                                    },
                                    {
                                        "id": 5,
                                        "name": "Secteur A-1-B"
                                    }
                                ]
                            },
                            {
                                "id": 3,
                                "name": "Territoire A-2",
                                "sectors": [
                                    {
                                        "id": 6,
                                        "name": "Secteur A-2-A"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
        # ===---
        return Response({
            "worlds": worlds_data,
            "valid": True
        })


class qpWorldView(APIView):

    def get(self, request, pk):
        zones_data = [
            {
                "id": 1,
                "name": "Zone A",
                "territories": [
                    {
                        "id": 2,
                        "name": "Territoire A-1",
                        "sectors": [
                            {
                                "id": 4,
                                "name": "Secteur A-1-A"
                            },
                            {
                                "id": 5,
                                "name": "Secteur A-1-B"
                            }
                        ]
                    },
                    {
                        "id": 3,
                        "name": "Territoire A-2",
                        "sectors": [
                            {
                                "id": 6,
                                "name": "Secteur A-2-A"
                            }
                        ]
                    }
                ]
            }
        ]
        # ===---
        return Response({
            "zones": zones_data,
            "valid": True
        })

