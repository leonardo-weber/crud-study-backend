from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Category
from .serializers import ProductSerializer

@api_view(['GET'])
def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_product_by_id(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id==id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        new_product = request.data
        serializer = ProductSerializer(data=new_product)

        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_product(request, id):
    if request.method == 'PUT':
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product(request, id):
    if request.method == 'DELETE':
        product = Product.objects.get(id=id)
        product.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
