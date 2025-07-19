from rest_framework.routers import DefaultRouter
from adventure.collection.viewsets.viewsets import CollectionViewSet
from django.urls import path, include

collection_router = DefaultRouter()
collection_router.register(r'collection', CollectionViewSet)

url_patterns = [
    path('', include(collection_router.urls)),
]