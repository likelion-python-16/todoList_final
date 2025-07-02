from django.db import models
from django.contrib.auth.models import User
from todo.models import Todo  # 대상 콘텐츠 모델

#  좋아요 모델
class Like(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)

    class Meta:
        unique_together = ("todo", "user")  # 중복 방지
        # 위의 속성은 중복 데이터를 아예 저장하지 못하게 막아주는 제약 조건입니다.

    def __str__(self):
        return f"{self.user.username} ❤️ {self.todo.name}"


#  북마크 모델
class Bookmark(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_marked = models.BooleanField(default=True)

    class Meta:
        unique_together = ("todo", "user")  # 중복 방지

    def __str__(self):
        return f"{self.user.username} 📌 {self.todo.name}"


#  댓글 모델
class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, through='CommentLike', related_name="liked_comments", blank=True)

    def __str__(self): #관리자 페이지에서 보여줄 문자표시
        return f"{self.user.username} 💬 {self.content[:20]}"


class CommentLike(models.Model): #댓글에 좋아요를 누른 기록을 저장할 CommentLike 모델을 정의한다. 이 모델은 Django의 기본 models.Model을 상속한다.
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    is_like = models.BooleanField(default=True)

    class Meta:
        unique_together = ("comment", "user")  # 중복 좋아요 방지

    def __str__(self):
        return f"{self.user.username} 💬 liked comment {self.comment.id}"