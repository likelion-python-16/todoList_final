from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from todo.serializers import TodoSerializer

from .models import Like, Bookmark, Comment
from .serializers import LikeSerializer, BookmarkSerializer, CommentSerializer
from todo.models import Todo


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"])
    def toggle(self, request, pk=None):
        todo = Todo.objects.get(pk=pk)
        user = request.user

        like, created = Like.objects.get_or_create(todo=todo, user=user)
        like.is_like = not like.is_like
        like.save()

        serializer = TodoSerializer(todo, context={"request": request})
        return Response(serializer.data)


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"])
    def toggle(self, request, pk=None):
        todo = Todo.objects.get(pk=pk)
        user = request.user

        bookmark, created = Bookmark.objects.get_or_create(todo=todo, user=user)
        bookmark.is_marked = not bookmark.is_marked
        bookmark.save()

        serializer = TodoSerializer(todo, context={"request": request})
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        todo_id = self.request.query_params.get("todo_pk")  # ✅ 쿼리스트링에서 받음
        return Comment.objects.filter(todo_id=todo_id).order_by("-created_at")

    def perform_create(self, serializer):
        todo_id = self.request.data.get("todo_pk")  # ✅ POST body에서 받음
        todo = Todo.objects.get(pk=todo_id)
        serializer.save(user=self.request.user, todo=todo)
