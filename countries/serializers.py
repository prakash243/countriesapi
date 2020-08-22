from rest_framework import serializers
from .models import Countries, Task, Product

class CountriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Countries
        fields = ('id', 'name', 'capital')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'