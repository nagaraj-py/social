from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from Ecartapp.models import Product
from Ecartapp.api.serializers import ProductSerializers
from rest_framework import filters
from django.db.models import Q

# class ProductView(viewsets.ModelViewSet):
#     serializer_class = ProductSerializers
#     queryset = Product.objects.all()

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [filters.OrderingFilter, filters.SearchFilter] 
    ordering_fields = ['price','name']
    search_fields = ['name', 'description','price']

   
    def get_queryset(self):
        queryset = super().get_queryset()
        price = self.request.query_params.get('price')
        name = self.request.query_params.get('name')

        # Instead of filtering directly, set the search and ordering query parameters
        self.search_term = name
        self.ordering_term = price

        return queryset

    def filter_queryset(self, queryset):
        # Apply filtering, searching, and ordering here
        if self.search_term:
            queryset = queryset.filter(name__icontains=self.search_term)
        if self.ordering_term:
            queryset = queryset.filter(price=self.ordering_term)
        
        return super().filter_queryset(queryset)

        # search_term = self.request.query_params.get('search')
        # if search_term:
        #     queryset = queryset.filter(
        #         Q(name__icontains=search_term) |
        #         Q(description__icontains=search_term) |
        #         Q(price=search_term)
        #         )
        
        # return queryset
