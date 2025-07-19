from adventure.activities.routers.routers import activities_router
from adventure.package.routers.routers import package_router
from adventure.collection.routers.routers import collection_router

from rest_framework.routers import DefaultRouter

adventure_router = DefaultRouter()

adventure_router.registry.extend(activities_router.registry)
adventure_router.registry.extend(package_router.registry)
adventure_router.registry.extend(collection_router.registry)
