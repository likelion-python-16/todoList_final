from .models import Todo
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy


# 목록 조회
class TodoListView(ListView):
    model = Todo
    template_name = "todo/list.html"
    context_object_name = "todos"
    ordering = ['-created_at']
    success_url = reverse_lazy('todo_List')


# 생성
class TodoCreateView(CreateView):
    model = Todo
    fields = ['name', 'description', 'complete', 'exp'] 
    template_name = "todo/create.html"
    success_url = reverse_lazy('todo_List')  


# 상세보기
class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo/detail.html"
    context_object_name = "todo"


# 수정
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['name', 'description', 'complete', 'exp']
    template_name = "todo/update.html"
    context_object_name = "todo"
    success_url = reverse_lazy('todo_List')


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
  logout(request) # 세션 초기화
  return redirect('todo_List')