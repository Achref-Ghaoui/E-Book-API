
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from .models import Book
from django.shortcuts import get_object_or_404
from .filtres import ProductFilter
from rest_framework.pagination import PageNumberPagination



# Create your views here.
@api_view(['GET'])
def get_all_products(request):
   products = Book.objects.all()
   serializer = ProductSerializer(products,many=True)
   return Response({"product":serializer.data})

@api_view(['GET'])
def get_by_id_product(request,pk):
   products = get_object_or_404(Book,id=pk)
   serializer = ProductSerializer(products,many=False)
   return Response({"product":serializer.data})


@api_view(['GET'])
def get_all_products_1(request):
   filterset=ProductFilter(request.GET,queryset=Book.objects.all().order_by("id"))
   serializer = ProductSerializer(filterset.qs,many=True)
   return Response({"products":serializer.data})

@api_view(['GET'])
def get_all_products_2(request):
   filterset=ProductFilter(request.GET,queryset=Book.objects.all().order_by("id"))
   count = filterset.qs.count()
   resPage=1
   paginator= PageNumberPagination()
   paginator.page_size=resPage
   queryset=paginator.paginate_queryset(filterset.qs,request)
   serializer = ProductSerializer(queryset,many=True)
   return Response({"products":serializer.data, "per page":resPage, "count":count})


@api_view(['GET'])
def get_by_id_product(request,pk):
   products = get_object_or_404(Book,id=pk)
   serializer = ProductSerializer(products,many=False)
   return Response({"product":serializer.data})

   

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_product(request):
    data = request.data
    serializer = ProductSerializer(data = data)

    if serializer.is_valid():
        product = Book.objects.create(**data,user=request.user)
        res = ProductSerializer(product,many=False)
 
        return Response({"product":res.data})
    else:
        return Response(serializer.errors)

