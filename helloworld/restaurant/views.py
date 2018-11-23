from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

from restaurant.serializers import RestaurantSerializer
from restaurant.models import Restaurant


class RestaurantView(APIView):
    _serializer_class = RestaurantSerializer

    def post(self, request):
        """
        Create a new reservation
        """
        serializer = self._serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Internal error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, user_id):
        restaurant = get_object_or_404(Restaurant, restaurant_id=user_id)
        serializer = self._serializer_class(restaurant)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("internal error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RestaurantListView(APIView):

    def get(self, request):
        rest_list = get_list_or_404(Restaurant)
        serializer = RestaurantSerializer(rest_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
