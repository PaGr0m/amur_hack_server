from django.shortcuts import render

# Create your views here.
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
# from .models import Beacon
# from .serializers import BeaconSerializer

# Create your views here.
from main.models import Urn


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def open_bin(request):
    print(request)
    yo = Urn.objects.where(UUID=request['id'])
    data = {'status': 'ok'}
    return Response(data, status=HTTP_200_OK)

# @csrf_exempt
# @api_view(["GET"])
# def beacons_index(request):
#     rest_list = Beacon.objects.all()
#     serializer = BeaconSerializer(rest_list, many=True)
#     return JsonResponse(serializer.data, safe=False)
#     # data = serializers.serialize('json', Beacon.objects.all())
#     # return Response(data, status=HTTP_200_OK)
