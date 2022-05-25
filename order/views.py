from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as st

from . import serializers
from .models import Order

class CreateOrderView(generics.CreateAPIView):
    serializer_class = serializers


class UserOrderList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        orders = user.orders.all()
        #orders = 



class UpdateOrderStatusView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def path(self, request, pk):
        status = request.data['status']
        if status not in ['in_process', 'closed']:
            return Response('Incalid Status', status=st.HTTP_400_BAD_REQUEST)
        order = Order.objects.get(pk=pk)
        order.status = status
        order.save()
        serializer = serializers.OrderSerializer(order)
        return Response(serializer.data,status=st.HTTP_206_PARTIAL_CONTENT)    