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

# @csrf_exempt
@api_view(["GET"])
# @permission_classes((AllowAny,))
def get_urns_workload(request):
    print("TRASH")
    for trashcan in Trashcan.objects.all():
        print("TRASH", trashcan)
        for urn in Urn.objects.filter(trashcan=trashcan):
            urn_dict = {
                str(urn.trash_type): urn.workload
            }
        trashcan_dict = {
            str(trashcan): urn_dict
        }

    return Response(trashcan_dict, status=HTTP_200_OK)



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def client_create(request):
    client = Client(login=request.data.get("login"),
                    password=request.data.get("password"),
                    fio=request.data.get("fio"),
                    nickname=request.data.get("nickname"),
                    score=request.data.get("score"))
    client.save()
    return Response("Client is create")


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


