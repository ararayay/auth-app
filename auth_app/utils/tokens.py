from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user) -> dict:
    refresh = RefreshToken.for_user(user)
    refresh.payload.update({
        'user_id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
    })
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
