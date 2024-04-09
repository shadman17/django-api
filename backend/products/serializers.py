from rest_framework import serializers
from rest_framework.reverse import reverse
from .validators import validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer

from .models import Product

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source= 'user', read_only = True)
    # related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    # my_discount = serializers.SerializerMethodField(read_only= True)
    edit_url = serializers.SerializerMethodField(read_only= True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    # email = serializers.EmailField(source='user.email', read_only=True)
    body = serializers.CharField(source='content')
     
    class Meta:
        model = Product
        fields = [
            'owner',
            # 'email',
            'url',
            'edit_url',
            'pk',
            'title',
            'body',
            'price',
            'sale_price',
            'path',
            # 'my_discount',
            # 'related_products',
        ]
        
    # def validate_title(self, value):
        # request = self.context.get('request')
        # user = request.user
        # print(request)
    #     qs = Product.objects.filter(user = user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value
        
    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email)
    #     # print(obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('emaill')
    #     return super().update(instance, validated_data)
        
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None

        
        return reverse("product-edit", kwargs={'pk': obj.pk}, request=request)
        
    # def get_my_discount(self, obj):
    #     # obj.user -> I can get user.username
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_discount()