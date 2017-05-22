from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from users.permissions import IsUserOrReadOnly
from users.serializers import CreateUserSerializers
# Create your views here.


class UserViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsUserOrReadOnly, )
    serializer_class = CreateUserSerializers

    def create(self, request, *args, **kwargs):
        self.permission_classes = (AllowAny, )
        return super(UserViews, self).create(request, *args, **kwargs)
