from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from main.models import Urn, Trashcan
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def update_urn(request):
    trashcan_id = request.data.get("id")
    trash = Trashcan.objects.get(id=trashcan_id)

    for urn in Urn.objects.filter(trashcan=trash):
        if urn.trash_type == "GLASS":
            urn.workload = request.data.get("glass")
        elif urn.trash_type == "PLASTIC":
            urn.workload = request.data.get("plastic")
        elif urn.trash_type == "PAPER":
            urn.workload = request.data.get("paper")
        elif urn.trash_type == "METAL":
            urn.workload = request.data.get("metal")
        elif urn.trash_type == "BATTERIES":
            urn.workload = request.data.get("batteries")
        elif urn.trash_type == "OTHER":
            urn.workload = request.data.get("other")
        urn.save()
    return Response("report")
