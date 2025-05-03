from django.urls import path
from .views import RequestMagicLinkView, VerifyMagicLinkView

urlpatterns = [
    path('request-magic-link/', RequestMagicLinkView.as_view()),
    path('verify-magic-link/', VerifyMagicLinkView.as_view()),
]
