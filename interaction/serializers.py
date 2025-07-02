from rest_framework import serializers
from .models import Like, Bookmark, Comment


# LikeSerializer
class LikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)  
    todo_name = serializers.CharField(source="todo.name", read_only=True) 

    class Meta:
        model = Like
        fields = ["id", "todo", "todo_name", "user", "username", "is_like"]
        read_only_fields = ["user"] 


# BookmarkSerializer
class BookmarkSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True) 
    todo_name = serializers.CharField(source="todo.name", read_only=True) 

    class Meta:
        model = Bookmark
        fields = ["id", "todo", "todo_name", "user", "username", "is_marked"]
        read_only_fields = ["user"]


# CommentSerializer 글에 대한 좋아요 기능을 함께 다루기 위한 설계방식
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True) 
    todo_name = serializers.CharField(source="todo.name", read_only=True) 
    like_count = serializers.SerializerMethodField() 
    is_liked = serializers.SerializerMethodField() 

    class Meta:
        model = Comment
        fields = [
            "id", 
            "todo",  
            "todo_name", 
            "user", 
            "username",  
            "content",  
            "created_at",  
            "like_count",  
            "is_liked",  
        ]
        read_only_fields = ["todo", "user", "created_at"] 


    def get_like_count(self, obj):
        return obj.likes.count()  

    def get_is_liked(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False


from .models import CommentLike

class CommentLikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True) 
    comment_content = serializers.CharField(source="comment.content", read_only=True) 

    class Meta:
        model = CommentLike
        fields = ['id', 'comment', 'comment_content', 'user', 'username', 'is_like', 'liked_at']
        read_only_fields = ['user', 'liked_at'] 
