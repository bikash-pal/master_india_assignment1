from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Catagories,SubCatagories,Products
from .serializers import CatagoriesSerializer,SubCatagoriesSerializer
@csrf_exempt
def catagories_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Catagories.objects.all()
        serializer = CatagoriesSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
def sub_catagories_list(request,catagorie):
    """
    List all code snippets, or create a new snippet.
    """
    print(catagorie)
    '''if request.method == 'GET':
        snippets = Catagories.objects.all()
        serializer = CatagoriesSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)'''
    sub_cattagorie=SubCatagories.objects.filter(catagorie_obj__catagorie=catagorie)
    serializer = SubCatagoriesSerializer(sub_cattagorie, many=True)
    return JsonResponse(serializer.data, safe=False)
