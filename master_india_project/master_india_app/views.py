from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
#from rest_framework.parsers import JSONParser
from .models import Catagories,SubCatagories,Products
from .serializers import CatagoriesSerializer,SubCatagoriesSerializer,ProductsSerializer

from rest_framework import status
from rest_framework.response import Response

@csrf_exempt
def catagories_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Catagories.objects.all()
        serializer = CatagoriesSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def sub_catagories_list(request,catagorie):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        sub_cattagorie=SubCatagories.objects.filter(catagorie_obj__catagorie=catagorie)
        serializer = SubCatagoriesSerializer(sub_cattagorie, many=True)
        return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def products_catagories_list(request,catagorie):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        products=Products.objects.filter(subCatagories_obj__catagorie_obj__catagorie=catagorie)
        serializer = ProductsSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def products_sub_catagories_list(request,sub_catagorie):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        products=Products.objects.filter(subCatagories_obj__subCatagories=sub_catagorie)
        serializer = ProductsSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def add_product(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    


