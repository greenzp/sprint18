from django.shortcuts import get_object_or_404
from order.models import Order
from authentication.models import CustomUser
from rest_framework import generics, status
from .serializers import OrderSerializer, CustomUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CustomUserView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


@api_view(['GET'])
def user_order_list(request, user_id):
    orders = Order.objects.filter(user=user_id)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_order_detail(request, user_id, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order in Order.objects.filter(user=user_id):
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    return Response(data={"detail": "Invalid order"}, status=status.HTTP_400_BAD_REQUEST)
