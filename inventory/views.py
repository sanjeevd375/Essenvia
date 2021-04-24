from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .exception import *
from .serializer import *
from . models import *

# Create your views here.
class InventoryView(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Inventory.objects.all()
        return queryset

    def get_object_from_all(self):
        return Inventory.objects.get(pk=self.kwargs.get('pk')
        )
    
    def create(self, request, *args, **kwargs):
        
        data = request.data
        
        serializer = InventorySerializer(data=data, context={"request": self.request})
        if serializer.is_valid():
            inventory_object = serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = InventoryListSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        
        data = request.data

        try:
            instance = self.get_object_from_all()
        except:
            return update_failed_exception("Object Doesn't exist.")

        serializer = InventorySerializer(instance=instance, data=data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object_from_all()
        except:
            return retrieve_failed_exception("Object Doesn't exist.")

        if instance is None:
            return retrieve_failed_exception("Object Doesn't exist.")

        serializer = InventorySerializer(instance=instance, context={"request": self.request})
        return Response(serializer.data)
