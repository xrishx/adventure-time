from company.homepage.routers.routers import homepage_router
from company.team.routers.routers import team_router

from rest_framework.routers import DefaultRouter

# New main router
router = DefaultRouter()

# Extend main router with other routers' URL patterns
router.registry.extend(homepage_router.registry)
router.registry.extend(team_router.registry)