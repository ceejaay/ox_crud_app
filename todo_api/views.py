from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from todo_items.models import Item
from .serializers import ItemSerializer

# Create your views here.


class ItemViewSet(viewsets.ViewSet):

    def items(self, request):
        if request.method == "POST":
            s = ItemSerializer(data=request.data)
            if s.is_valid():
                s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        elif request.method == "GET":
            i = Item.objects.all()
            seri = ItemSerializer(i, many=True)
            return Response(seri.data, status=status.HTTP_200_OK)


    def single_item(self, request, pk):
        todo_item = get_object_or_404(Item, id=pk)
        if request.method == "GET":
            seri = ItemSerializer(todo_item)
            return Response(seri.data, status=status.HTTP_200_OK)
        elif request.method == "DELETE":
            todo_item.delete()
            delete_seri = ItemSerializer(todo_item)
            return Response(delete_seri.data, status=status.HTTP_204_NO_CONTENT)
        elif request.method == "PUT":
            put_serializer = ItemSerializer(todo_item, data=request.data)
            if put_serializer.is_valid():
                put_serializer.save()
                return Response(put_serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(put_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


