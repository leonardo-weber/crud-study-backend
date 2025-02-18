from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer

class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post (self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):

    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

