from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    DislikeViewSet,
    InboxViewSet,
    LikeViewSet,
    MatchViewSet,
    ProfileViewSet,
    SettingViewSet,
    UserPhotoViewSet,
)

router = DefaultRouter()
router.register("match", MatchViewSet)
router.register("inbox", InboxViewSet)
router.register("profile", ProfileViewSet)
router.register("dislike", DislikeViewSet)
router.register("setting", SettingViewSet)
router.register("like", LikeViewSet)
router.register("userphoto", UserPhotoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
