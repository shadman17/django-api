from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.authentication import TokenAuthentication

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] #Permission Ordering matters
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] #Permission Ordering matters
    
    # Product.objects.get(pk='abc')
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] #Permission Ordering matters
    
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] #Permission Ordering matters
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

class ProductMixinView(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'          
    
    def get(self, request, *args, **kwargs):
        print(args, kwargs) #{} {'pk': 3}
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@api_view(['GET', 'POST'])    
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    
    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk) 
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)
        
    if method == "POST":
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        
        return Response({"invalid": "Not good data"}, status = 400)
