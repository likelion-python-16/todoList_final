from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser


# 전체보기
# class TodoListAPI(APIView):
#     def get(self, request):
#         todos = Todo.objects.all().order_by("-pk")
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)


# 생성하기
# class TodoCreateAPI(APIView):
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request):
#         serializer = TodoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         todo = serializer.save()
#         return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)


# 상세보기
# class TodoRetrieveAPI(APIView):
#     def get(self, request, pk):
#         try:
#             todo = Todo.objects.get(pk=pk)
#         except Todo.DoesNotExist:
#             return Response(
#                 {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)


# 수정하기
# class TodoUpdateAPI(APIView):
#     def put(self, request, pk):
#         try:
#             todo = Todo.objects.get(pk=pk)
#         except Todo.DoesNotExist:
#             return Response(
#                 {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = TodoSerializer(todo, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         todo = serializer.save()
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)

#     def patch(self, request, pk):
#         try:
#             todo = Todo.objects.get(pk=pk)
#         except Todo.DoesNotExist:
#             return Response(
#                 {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = TodoSerializer(todo, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         todo = serializer.save()
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)


# 삭제하기
# class TodoDeleteAPI(APIView):
#     def delete(self, request, pk):
#         try:
#             todo = Todo.objects.get(pk=pk)
#         except Todo.DoesNotExist:
#             return Response(
#                 {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
#             )

#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# APIView는 DRF의 가장 기본 클래스. HTTP 메서드(GET, POST 등)를 
# 직접 정의하며, request, response, permission 처리 기능 제공

# GenericAPIView는 GenericAPIView는 APIView를 상속하면서
# 자주 사용하는 기능들을 미리 만들어 놓은 클래스입니다.
# 예를 들어,
# queryset: 어떤 데이터를 불러올지 설정
# serializer_class: 어떤 형태로 데이터를 주고받을지 설정
# 이런 기능들을 쉽게 쓸 수 있도록 도와줍니다.


# REST Framework_GenericAPIView
# class TodoGenericsListAPI(generics.ListAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class TodoGenericsCreateAPI(generics.CreateAPIView):
#     serializer_class = TodoSerializer


# class TodoGenericsRetrieveAPI(generics.RetrieveAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class TodoGenericsUpdateAPI(generics.UpdateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class TodoGenericsDeleteAPI(generics.DestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# Generics list + create
# class TodoGenericsListCreateAPI(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# # Generics retriver + update + delete
# class TodoGenericsRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer



from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated  # 권한 설정용
from rest_framework.authentication import SessionAuthentication  # 인증 방식


# ViewSet은
# CRUD 기능을 한 곳에 모아서 간편하게 만들 수 있도록 도와주는 클래스입니다.
# viewset하나면 자동으로 list, create, retrieve(상세조회), update(수정), destroy(삭제) 기능이 생깁니다.

# REST Framework_ViewSets
class TodoViewSet(viewsets.ModelViewSet):
    # queryset = Todo.objects.all().order_by("-created_at") 있으면 basename 생략 가능
    serializer_class = TodoSerializer
    
    # 인증 방식 설정: Django 로그인 세션 사용
    authentication_classes = [SessionAuthentication]
    # 권한 설정: 로그인된 사용자만 이 API 사용 가능
    permission_classes = [IsAuthenticated]

    # 정렬된 쿼리셋 반환 (최신 생성일 순)
    def get_queryset(self):  
        qs = Todo.objects.all().order_by("-created_at")
        print("정렬된 queryset preview:", list(qs[:3]))  # 서버 로그 확인용
        return qs

# get_queryset(): 필요할 때 데이터를 필터링해서 가져올 수 있는 함수
# /todo/viewsets/view/

# 로그아웃 API (세션 기반 로그아웃 처리)
class CustomLogoutAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "로그아웃 완료"}, status=status.HTTP_200_OK)
