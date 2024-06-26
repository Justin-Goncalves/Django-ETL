from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
import pandas

# Create your views here.
@api_view(['GET', 'POST'])
def customer_details(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    elif request.method == 'POST':
        if request.FILES:
            file = pandas.read_csv(request.FILES['data']).to_dict(orient="records")
            serializer = CustomerSerializer(data=file, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response('Successfully Uploaded :^)')