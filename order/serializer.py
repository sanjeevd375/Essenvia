from rest_framework import serializers
from .models import *
import json

class OrderSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super(OrderSerializer, self).to_representation(instance)
        return ret

    class Meta:
        model = Order
        exclude = ()
