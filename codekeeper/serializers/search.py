from rest_framework import serializers


class SearchDocsSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=100)
    id = serializers.CharField(max_length=100)
    item_id = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)


class SearchResultsSerializer(serializers.Serializer):
    docs = SearchDocsSerializer(many=True)
    numFound = serializers.IntegerField()



class SearchSerializer(serializers.Serializer):
    result = SearchResultsSerializer()

