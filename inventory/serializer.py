from rest_framework import serializers
from .models import *

class InventorySerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super(InventorySerializer, self).to_representation(instance)
        return ret

    class Meta:
        model = Inventory
        exclude = ()

class InventoryListSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super(InventoryListSerializer, self).to_representation(instance)
        return ret

    class Meta:
        model = Inventory
        exclude =  (
        )