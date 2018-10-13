from django.core.exceptions import ValidationError
from django.shortcuts import render

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from main.models import Urn, Trashcan, Client


# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_urns_workload(request):
    all_list = []
    trashcan_dict = {}
    urn_dict = {}
    for trashcan in Trashcan.objects.all():
        for urn in Urn.objects.filter(trashcan=trashcan):
            urn_dict.update({
                str(urn.trash_type): urn.workload

            })

        urn_dict.update({
            "name": trashcan.location.name,
            "longitude": trashcan.location.longitude,
            "latitude": trashcan.location.latitude
        })
        # trashcan_dict = {
        #     str(trashcan): urn_dict,
        #     "longitude": trashcan.location.longitude,
        #     "latitude": trashcan.location.latitude
        # }
        all_list.append(trashcan_dict)

    return Response(urn_dict)


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
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def open_bin(request):
    try:
        urn = Urn.objects.filter(UUID=request.data.get('UUID')).first()
    except ValidationError:
        data = {'status': 'not UUID'}
        return Response(data, status=HTTP_200_OK)
    if urn:
        data = {'status': 'ok'}
        # сигнал на открытие
    else:
        data = {'status': 'urn not found'}
    return Response(data, status=HTTP_200_OK)


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
