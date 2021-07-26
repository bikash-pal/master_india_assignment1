from django.urls import path
from . import views

urlpatterns = [
    path('catagories/', views.catagories_list),
    path('sub_catagories/<slug:catagorie>/', views.sub_catagories_list),
    
]