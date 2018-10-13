from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from main.models import Urn, Trashcan, Client


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_urns_workload(request):
    all_list = []
    for trashcan in Trashcan.objects.all():
        trashcan_dict = {}
        trashcan_dict.update({
            "longitude": trashcan.location.longitude,
            "latitude": trashcan.location.latitude,
            "name": trashcan.location.name
        })

        for urn in Urn.objects.filter(trashcan=trashcan):
            trashcan_dict.update({
                str(urn.trash_type): urn.workload
            })

        all_list.append(trashcan_dict)

    return Response(all_list)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def client_create(request):
    client = Client(email=request.data.get("email"),
                    password=request.data.get("pass"),
                    firstname=request.data.get("fname"),
                    surname=request.data.get("lname"),
                    phone=request.data.get("phone"))
    client.save()
    report = {
        "token": client.token
    }
    return Response(report)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def authorization(request):
    email = request.data.get("email")
    password = request.data.get("pass")

    client = Client.objects.get(email=email)
    if client.password == password:
        report = {
            "fname": client.firstname,
            "lname": client.surname,
            "token": client.token,
            "phone": client.phone,
            "score": client.score
        }
    else:
        report = {
            "answer": "error"
        }
    return Response(report)
