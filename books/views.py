from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import FileResponse, HttpResponseNotFound, HttpResponse
from django.conf import settings
import os
from .models import Book
from .serializers import *
import mimetypes
# Create your views here.
@api_view(['GET','POST'])
def book_list(request):
    if request.method=='GET':
        data = Book.objects.all()
        serializer = BookSerializer(data,context={'request':request},many=True)

        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET'])
def book_list_price(request):
    sort_by = request.GET.get('sort_by','price')
    data = Book.objects.all().order_by(sort_by)
    serializer = BookSerializer(data,context={'request':request},many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_list_rating(request):
    sort_by = request.GET.get('sort_by','-average_rating')
    data = Book.objects.all().order_by(sort_by)
    serializer = BookSerializer(data,context={'request':request},many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def book_list_category(request,category):
    
    data = Book.objects.filter(categories=category)
    serializer = BookSerializer(data,context={'request':request},many=True)
    return Response(serializer.data)
    


def serve_book_cover(request, filename):
    book_covers_directory = 'book_covers'
    file_path = os.path.join(settings.MEDIA_ROOT, book_covers_directory, filename)

    if not os.path.isfile(file_path):
        return HttpResponseNotFound('The requested book cover does not exist.')

    try:
        with open(file_path, 'rb') as f:
            content_type, _ = mimetypes.guess_type(file_path)
            if content_type is None:
                content_type = 'application/octet-stream'
            response = HttpResponse(f.read(), content_type=content_type)
            return response
    except IOError:
        return HttpResponseNotFound('An error occurred while reading the book cover.')