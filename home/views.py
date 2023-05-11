from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

from .serializers import *


class HandleFileUpload(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = FileListSerializer(data=data)

            if not serializer.is_valid():
                return Response({"message": serializer.errors,}, status=400)

            serializer.save()

            return Response({"message": "File uploaded successfully"}, status=200)

        except Exception as e:
            return Response({"message": str(e)}, status=400)
