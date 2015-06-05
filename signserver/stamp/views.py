from stamp.models import Stamp
from stamp.serializers import StampSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StampAdd(APIView):
    def get(self, request, format=None):
        return Response("{}")

    def post(self, request, format=None):
        serializer = StampSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "refid" : serializer.data["pk"],
            }
            return Response(data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"refid" : -1 }, status=status.HTTP_400_BAD_REQUEST)

class StampDetail(APIView):
    """
    Retrieve, update or delete a Stamp instance.
    """
    def get_object(self, refid):
        try:
            return Stamp.objects.get(pk=refid)
        except Stamp.DoesNotExist:
            raise Http404

    def get(self, request, refid, format=None):
        stamp = self.get_object(refid)
        serializer = StampSerializer(stamp)
        return Response(serializer.data)

    def put(self, request, refid, format=None):
        stamp = self.get_object(refid)
        serializer = StampSerializer(stamp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, refid, format=None):
        stamp = self.get_object(refid)
        stamp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)