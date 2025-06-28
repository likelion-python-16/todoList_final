from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from todo.models import Todo
from interaction.models import Like, Bookmark, Comment


@login_required
def todo_detail_with_interaction(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    user = request.user

    # 좋아요 여부 및 총 수
    like_obj = Like.objects.filter(todo=todo, user=user).first()
    like_count = Like.objects.filter(todo=todo, is_like=True).count()

    # 북마크 여부
    bookmark_obj = Bookmark.objects.filter(todo=todo, user=user).first()

    # 댓글 목록
    comments = Comment.objects.filter(todo=todo).order_by("-created_at")

    context = {
        "todo": todo,
        "like_obj": like_obj,
        "like_count": like_count,
        "bookmark_obj": bookmark_obj,
        "comments": comments,
    }

    return render(request, "interaction/todo_detail.html", context)
