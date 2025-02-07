"""
URL configuration for chat_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import *
from chats.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/users/', UserListView.as_view()),
    path('api/v1/current_user/', GetCurrentUserView.as_view()),
    path('api/v1/chats/', ChatListView.as_view()),
    path('api/v1/chats/<int:pk>/', ChatView.as_view()),
    path('api/v1/messages/', MessageListView.as_view()),
    path('api/v1/login/', TokenObtainPairView.as_view()),
    path('api/v1/register/', UserCreateView.as_view()),


]
