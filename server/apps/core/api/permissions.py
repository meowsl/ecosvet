from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey


class HasApiKeyOrIsAuthenticated(HasAPIKey):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or bool(
            request.user and request.user.is_authenticated
        )
