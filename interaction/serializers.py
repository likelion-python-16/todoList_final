from rest_framework import serializers
from .models import Like, Bookmark, Comment


#  LikeSerializer
class LikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    todo_name = serializers.CharField(source="todo.name", read_only=True)

    class Meta:
        model = Like
        fields = ["id", "todo", "todo_name", "user", "username", "is_like"]
        read_only_fields = ["user"]


#  BookmarkSerializer
class BookmarkSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    todo_name = serializers.CharField(source="todo.name", read_only=True)

    class Meta:
        model = Bookmark
        fields = ["id", "todo", "todo_name", "user", "username", "is_marked"]
        read_only_fields = ["user"]


#  CommentSerializer
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    todo_name = serializers.CharField(source="todo.name", read_only=True)
    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        # fields = "__all__"
        fields = [
            "id",  # Todo 기본키
            "todo",  # 외래키 (댓글 또는 좋아요 대상)
            "todo_name",  # 연결된 Todo의 이름 (source로 처리)
            "user",  # 작성자 또는 요청 유저
            "username",  # 작성자 이름 (source로 처리)
            "content",  # 댓글 내용
            "created_at",  # 작성 시간
            "like_count",  # 좋아요 수 (SerializerMethodField)
            "is_liked",  # 내가 좋아요 눌렀는지 여부 (SerializerMethodField)
        ]
        read_only_fields = ["todo", "user", "created_at"]
        # 클라이언트 → 서버로 데이터 전송 시 무시되는 필드
        # serializer.save()에서는 내부적으로 값을 설정할 수 있음
        # 폼에서 사용자가 수정할 수 없어야 할 필드를 명확히 구분하는 용도로 사용됨

    def get_like_count(self, obj):
        return (
            obj.likes.count()
        )  # → Comment 모델에 related_name='likes'인 Like 모델 연결 필요

    def get_is_liked(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False
