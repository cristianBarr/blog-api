from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    """
    Extiende el modelo User de Django para agregar campos adicionales.
    Relación 1 a 1: Cada usuario tiene exactamente un perfil.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,  # Si se elimina el User, se elimina su perfil
        related_name='profile'  # Para acceder desde User: user.profile
    )
    bio = models.TextField(
        blank=True,  # El campo puede estar vacío
        help_text="Descripción breve del usuario (máx. 500 caracteres)"
    )
    avatar = models.ImageField(
        upload_to='avatars/',  # Guarda en MEDIA_ROOT/avatars/
        blank=True,
        null=True,
        help_text="Imagen de perfil (recomendado 200x200px)"
    )

    def __str__(self):
        return f"Perfil de {self.user.username}"

    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuarios'


class Article(models.Model):
    """
    Modelo para artículos/blog posts.
    Campos básicos: título, contenido y fecha de creación.
    """
    title = models.CharField(
        max_length=200,
        help_text="Título del artículo (máx. 200 caracteres)"
    )
    content = models.TextField(
        help_text="Contenido completo del artículo"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,  # Fecha automática al crear
        help_text="Fecha de creación del artículo"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['-created_at']  # Ordenar por fecha descendente