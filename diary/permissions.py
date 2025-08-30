# diary/permissions.py
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешает доступ только владельцу объекта.
    Просмотр (GET) разрешён всем авторизованным пользователям.
    Изменение и удаление — только владельцу.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем безопасные методы всем (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Только владелец может изменять или удалять
        return obj.user == request.user
