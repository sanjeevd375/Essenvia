from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import *
from .models import *
from inventory.models import *
import json

# Create your views here.
class OrderView(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Order.objects.all()
        return queryset

    def get_object_from_all(self):
        return Order.objects.get(pk=self.kwargs.get('pk')
        )

    def create(self, request, *args, **kwargs):
        
        data = request.data

        is_available, message = Inventory.check_item_availability(data=data['order_details'])
        
        if is_available:
            
            data = {
                "order_details": json.dumps(data['order_details']),
                "customer_details": json.dumps(data['customer_details']),
                "delivery_dist": data['delivery_dist']
            }
            
            serializer = OrderSerializer(data=data, context={"request": self.request})
            if serializer.is_valid():
                order_object = serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors)
        
        else:
            return Response({
                "message": message
            })    