from rest_framework import serializers




class InventorySerializer(serializers.Serializer):


    id = serializers.CharField(max_length=200, read_only=True)
    name = serializers.CharField(max_length=200)
    status = serializers.CharField(max_length=200)
    due_date = serializers.CharField(max_length=200)


