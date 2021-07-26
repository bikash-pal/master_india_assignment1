from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Catagories,SubCatagories,Products
from .serializers import CatagoriesSerializer,SubCatagoriesSerializer,ProductsSerializer
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
    sub_cattagorie=SubCatagories.objects.filter(catagorie_obj__catagorie=catagorie)
    serializer = SubCatagoriesSerializer(sub_cattagorie, many=True)
    return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def products_catagories_list(request,catagorie):
    """
    List all code snippets, or create a new snippet.
    """
    products=Products.objects.filter(subCatagories_obj__catagorie_obj__catagorie=catagorie)
    serializer = ProductsSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def products_sub_catagories_list(request,sub_catagorie):
    """
    List all code snippets, or create a new snippet.
    """
    products=Products.objects.filter(subCatagories_obj__subCatagories=sub_catagorie)
    serializer = ProductsSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)

