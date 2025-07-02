from company.homepage.routers.routers import homepage_router
from company.team.routers.routers import team_router
from company.popup.routers.routers import popup_router
from company.privacypolicy.routers.routers import privacypolicy_router
from company.termsconditions.routers.routers import termsconditions_router
from company.visainformation.routers.routers import visainformation_router
from company.legaldocs.routers.routers import legaldocs_router

from rest_framework.routers import DefaultRouter

# New main router
router = DefaultRouter()

# Extend main router with other routers' URL patterns
router.registry.extend(homepage_router.registry)
router.registry.extend(team_router.registry)
router.registry.extend(popup_router.registry)
router.registry.extend(privacypolicy_router.registry)
router.registry.extend(termsconditions_router.registry)
router.registry.extend(visainformation_router.registry)
router.registry.extend(legaldocs_router.registry)