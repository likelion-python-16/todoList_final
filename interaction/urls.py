from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import LikeViewSet, BookmarkViewSet, CommentViewSet

router = DefaultRouter()
router.register(r"likes", LikeViewSet, basename="like")
router.register(r"bookmarks", BookmarkViewSet, basename="bookmark")
router.register(r"comments", CommentViewSet, basename="comment")  # ✅ 수정

urlpatterns = [
    path("", include(router.urls)),
]
