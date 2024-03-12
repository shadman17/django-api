from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    # """
    # get -> list -> Queryset
    # get -> retrive -> Product Instance Detail View
    # post -> create -> New Instance
    # put -> update 
    # patch -> partial update
    # delete -> destroy
    # """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default

class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    # """
    # get -> list -> Queryset
    # get -> retrive -> Product Instance Detail View
    # """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default