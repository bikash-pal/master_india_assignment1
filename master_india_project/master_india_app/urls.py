from django.urls import path
from . import views

urlpatterns = [
    path('catagories/', views.catagories_list),
    path('sub_catagories/<slug:catagorie>/', views.sub_catagories_list),
    path('products_catagories/<slug:catagorie>/', views.products_catagories_list),
    path('products_sub_catagorie/<slug:sub_catagorie>/', views.products_sub_catagories_list),
    #path('products_sub_catagorie/<slug:sub_catagorie>/', views.products_sub_catagories_list),
    
]
