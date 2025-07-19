"""
URL configuration for adventuretime project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from adventuretime.routers.adventure_routers import adventure_router
from adventuretime.routers.company_routers import company_router
from booking.routers.routers import urlpatterns as booking_router
from queries.routers.routers import urlpatterns as queries_router
from reviews.routers.routers import urlpatterns as reviews_router
from blog.routers.routers import urlpatterns as blog_router
from faqs.routers.routers import urlpatterns as faqs_router
from users.routers.routers import urlpatterns as users_router

schema_view = get_schema_view(
    openapi.Info(
        title="Adventure Time API",
        default_version='v1',
        description="Backend Project with Django REST Framework",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rishavshrestha6679@gmail.com"),
        license=openapi.License(name="No License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),
    path('adventure/', include(adventure_router.urls)),
    path('company/', include(company_router.urls)),
    path('booking/', include(booking_router)),
    path('queries/', include(queries_router)),
    path('reviews/', include(reviews_router)),
    path('blog/', include(blog_router)),
    path('faqs/', include(faqs_router)),
    path('users/', include(users_router)),
    path('api/auth/', include('rest_framework.urls')),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# During development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)