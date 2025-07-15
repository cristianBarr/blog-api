from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from articles import views
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView  

# Vista de bienvenida para la ruta base '/api/'
def api_welcome(request):
    return JsonResponse({"message": "Bienvenido a la API del Blog", "endpoints": {
        "auth": "/api/auth/",
        "articles": "/api/articles/",
        "docs": "/api/docs/"
    }})

urlpatterns = [
    # Panel de administración de Django (default)
    path('admin/', admin.site.urls),
    
    # Ruta base de la API (personalizada)
    path('api/', api_welcome, name='api-root'),
    
    # Auth: Rutas de autenticación (JWT)
    path('api/auth/register/', views.RegisterView.as_view(), name='auth-register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='auth-login'),  # Obtiene token JWT
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='auth-refresh'),  # Refresca token JWT
    
    # Artículos: CRUD de artículos
    path('api/articles/', views.ArticleListCreate.as_view(), name='article-list'),
    
    # Perfil de usuario
    path('api/profile/', views.UserProfileView.as_view(), name='user-profile'),
    
    # Documentación automática (Swagger/OpenAPI)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # Genera el esquema OpenAPI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Interfaz visual
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Sirve archivos multimedia en desarrollo