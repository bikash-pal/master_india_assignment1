from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Catagories(models.Model):
    catagorie=models.CharField(max_length=100,null=True)
class SubCatagories(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    catagorie = models.ForeignKey(Catagories, on_delete=models.CASCADE)
    subCatagories=models.CharField(max_length=100,null=True)
class Products(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    subCatagories = models.ForeignKey(SubCatagories, on_delete=models.CASCADE)
    products=models.CharField(max_length=100,null=True)

