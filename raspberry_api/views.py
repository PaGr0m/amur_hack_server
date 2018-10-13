from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from main.models import Urn, Trashcan

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def update_urn(request):
    trashcan_id = request.data.get("id")
    print(trashcan_id)

    trash = Trashcan.objects.get(id=trashcan_id)
    print(trash)

    qwe = Urn.objects.get(trashcan=trash)
    print(qwe)

    # urns = Urn.objects.get(trashcan="trashcan_id")

    # for el in Urn.objects.all():
    #     print(">>> ", el.id)
    #
    # print(request.data.get("id"))
    # print(request.data.get("plastic"))

    return Response(qwe)


    # data = {
    #     'id': trash_id,
    #     'plastic': self.plastic,
    #     'metal': self.metal,
    #     'glass': self.glass,
    #     'paper': self.paper,
    #     'battery': self.battery,
    #     'unsorted': self.unsorted
    # }
