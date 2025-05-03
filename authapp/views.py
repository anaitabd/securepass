from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import MagicLinkToken
from .utils import send_magic_link
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RequestMagicLinkView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user, _ = User.objects.get_or_create(email=email, username=email)
        token = MagicLinkToken.objects.create(user=user)
        send_magic_link(email, token.token)
        return Response({'detail': 'Magic link sent'}, status=200)

class VerifyMagicLinkView(APIView):
    def get(self, request):
        token_str = request.GET.get('token')
        try:
            token = MagicLinkToken.objects.get(token=token_str)
            if not token.is_valid():
                return Response({'error': 'Token expired or already used'}, status=400)
            token.is_used = True
            token.save()
            refresh = RefreshToken.for_user(token.user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        except MagicLinkToken.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=400)