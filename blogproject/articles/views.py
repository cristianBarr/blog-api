from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import render
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados

class ArticleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
