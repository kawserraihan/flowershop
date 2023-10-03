from django.shortcuts import render
from app1.models import Inventory
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.authtoken.models import Token
#from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
#from itertools import chain
from rest_framework import serializers, status
from rest_framework.generics import ListAPIView
from django.db.models.signals import post_save
from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from django.db.models import Sum, Count
from django.conf import settings
from flowerAPI.serializers import *
from django.http import JsonResponse
from django.http import HttpResponseRedirect

from rest_framework.exceptions import NotFound

from app1.models import *
from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework import viewsets

from rest_framework.exceptions import NotFound

from flowerAPI.firebase_client import FirebaseClient
from flowerAPI.serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response


class InventoryViewSet(viewsets.ModelViewSet):
    client = FirebaseClient()
    
    def create(self, request, *args, **kwargs):
        serializer = InventorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.create(serializer.data)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )



