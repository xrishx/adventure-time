from rest_framework.routers import DefaultRouter
from adventure.package.viewsets.viewsets import PackageViewSet
from django.urls import path, include

package_router = DefaultRouter()
package_router.register(r'package', PackageViewSet)

urlpatterns = [
    path('', include(package_router.urls)),
]