from django.shortcuts import render
from .models import Carlist, Showroomlist, Review
from django.http import JsonResponse
from .serializers.serializers import CarSerializer, ShowroomSerializer, ReviewSerializer
from .serializers.permissions import AdminOrReadOnlyPermission, ReviewUserorReadOnlyPermission
from .serializers.throtlling import ReviewDetailThrottle, ReviewListThrottle
from .serializers.pagination import ReviewListPagination
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework import generics
from rest_framework.exceptions import ValidationError 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        cars = Carlist.objects.get(pk=pk)
        useredit = self.request.user
        Review_queryset = Review.objects.filter(car=cars, apiuser= useredit)
        if Review_queryset.exists():
            raise ValidationError('You have already reviewed this car')
        serializer.save(car=cars) 


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    # authentication_classes = [JWTAuthentication]
    throttle_classes=[ReviewListThrottle, AnonRateThrottle]
    permission_classes = [AdminOrReadOnlyPermission]
    pagination_class = ReviewListPagination

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(car=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    throttle_classes=[ReviewDetailThrottle, AnonRateThrottle]
    permission_classes = [ReviewUserorReadOnlyPermission]

    

class Showroom_Viewset(viewsets.ModelViewSet):
    queryset = Showroomlist.objects.all()
    serializer_class = ShowroomSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'showroom_viewset_scope'

class ShowroomView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    def get(self, request):
        showroom = Showroomlist.objects.all()
        serializer = ShowroomSerializer(showroom, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ShowroomSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: return Response(serializer.errors)

class ShowroomDetailView(APIView):

    def get(self, request, pk):
        try:
            showroom = Showroomlist.objects.get(pk=pk)
            serializer = ShowroomSerializer(showroom)
            return Response(serializer.data)
        except:
             return Response({"error": "Not found"}, status=status.HTTP_404_NOT)

    def put(self, request, pk):
        showroom = Showroomlist.objects.get(pk=pk)
        serializer = ShowroomSerializer(showroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
             return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
 
    def delete(self, request, pk):
        showroom = Showroomlist.objects.get(pk=pk)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


@api_view(['GET', 'POST'])
def car_list_view(request):
    if request.method == 'GET':
        car = Carlist.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail_view(request, pk):
    if request.method == 'GET':
        try:
            car = Carlist.objects.get(pk=pk)
        except: return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        car = Carlist.objects.get(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        car = Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

