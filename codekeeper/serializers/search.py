from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=200)
    id = serializers.CharField(max_length=100)
    fields = ("type", "id")