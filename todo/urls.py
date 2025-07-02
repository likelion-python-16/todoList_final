from django.urls import path, include
from . import views
# from .views import todo_Main, TodoListView, TodoCreateView, TodoDetailView, TodoUpdateView
from .api_views import *
from rest_framework.routers import DefaultRouter
from . import views, api_views

router = DefaultRouter()
router.register(r"view", TodoViewSet, basename="todo")

app_name ="todo"

urlpatterns = [
	#path("list/", views.todo_list, name="todo_List"), #데이터 작동 테스트용

    # 탬플릿View
    path("list/", views.TodoListView.as_view(), name="todo_List"),
    path("create/", views.TodoCreateView.as_view(), name="todo_Create"),
    path("detail/<int:pk>/", views.TodoDetailView.as_view(), name="todo_Detail"),
    path("update/<int:pk>/", views.TodoUpdateView.as_view(), name="todo_Update"), 

    # APIView
    # path("api/list/", api_views.TodoListAPI.as_view(), name="todo_api_list"),
    # path("api/create/", api_views.TodoCreateAPI.as_view(), name="todo_api_create"),
    # path("api/retrieve/<int:pk>/", api_views.TodoRetrieveAPI.as_view(), name="todo_api_retrieve"),
    # path("api/update/<int:pk>/", api_views.TodoUpdateAPI.as_view(), name="todo_api_update"),
    # path("api/delete/<int:pk>/", api_views.TodoDeleteAPI.as_view(), name="todo_api_delete"),

    # GenericAPIView
    # path("generics/create/", TodoGenericsCreateAPI.as_view()),
	# path("generics/list/", TodoGenericsListAPI.as_view()),
	# path("generics/retrieve/<int:pk>/", TodoGenericsRetrieveAPI.as_view()),
	# path("generics/update/<int:pk>/", TodoGenericsUpdateAPI.as_view()),
	# path("generics/delete/<int:pk>/", TodoGenericsDeleteAPI.as_view()),

    # path("generics/", TodoGenericsListCreateAPI.as_view(), name="todo_generics_list_create"),
    # path("generics/<int:pk>/", TodoGenericsRetrieveUpdateDeleteAPI.as_view(), name="todo_generics_detail"),

    
    # ViewSet
    path("viewsets/", include(router.urls)),
    path("api/custom-logout/", api_views.CustomLogoutAPI.as_view(), name="custom_logout"),
] 
