from django.shortcuts import render
from .serializers import NotificationSerializer
from rest_framework import generics
from rest_framework import permissions

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.notifications.all().order_by('-timestamp')