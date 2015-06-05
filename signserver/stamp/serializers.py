from django.forms import widgets
from rest_framework import serializers
from stamp.models import Stamp


class StampSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True) #pk is primary key of Model
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        try:
            if data['title']:
                pass
        except:
            raise serializers.ValidationError("no title")
        
        return data

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Stamp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance