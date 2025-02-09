"""
URL configuration for bookmark_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from bookmarks.views import BookmarkViewSet
from bookmarks.views import *
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Bookmark Tracker!")

router = DefaultRouter()
router.register(r'bookmarks', BookmarkViewSet, basename='bookmark')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    path('api/', include(router.urls)),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/bookmarks/list/', BookmarkListView.as_view(), name='bookmark-list'),
    path('api/signup/', UserRegistrationView.as_view(), name='signup'),

]
