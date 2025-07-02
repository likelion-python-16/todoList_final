from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo/", include("todo.urls")),
    path('', lambda request: redirect('todo:todo_List')),
    path('api-auth/', include('rest_framework.urls')),
    path("accounts/", include("django.contrib.auth.urls")), #배포할때 필요 templates/regustration/logged_out.html
    
    # interaction 앱 API
    path('api/interaction/', include('interaction.urls')),

    # OpenAPI 3.0 schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path('interaction/', include('interaction.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


