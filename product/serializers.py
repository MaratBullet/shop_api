from rest_framework import serializers

from product.models import Category, NewProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewProduct
        fields = '__all__'

class ProductlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewProduct
        fields = ('name', 'price', 'image')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['products'] = ProductSerializer (instance.products.all(),
        many=True.data)
        return representation