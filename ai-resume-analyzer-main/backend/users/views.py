from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import RegisterSerializer, UserSerializer

import traceback

# Get the custom User model
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            traceback.print_exc()

            return Response(
                {
                    "error": str(e),
                    "type": type(e).__name__,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ProtectedRouteView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response({
            "message": "You have successfully accessed a protected route!",
            "user": serializer.data
        })