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
    likes = models.ManyToManyField(User, related_name="liked_comments", blank=True)

    def __str__(self):
        return f"{self.user.username} 💬 {self.content[:20]}"
