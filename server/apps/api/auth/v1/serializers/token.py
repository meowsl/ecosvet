from rest_framework import exceptions, serializers
from rest_framework_simplejwt.serializers import (
    TokenVerifySerializer as BaseTokenVerifySerializer,
)


class TokenVerifySerializer(BaseTokenVerifySerializer):
    token = serializers.CharField(
        required=False,
        allow_null=True,
    )

    def validate_token(self, token):
        if not token:
            raise exceptions.NotAuthenticated(
                "Время Вашего сеанса истекло. Войдите в систему еще раз."
            )
        return token
