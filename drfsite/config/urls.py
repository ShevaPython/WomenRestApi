"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from women.views import WomenViewSet,WomenReadonlySet
from rest_framework import routers

# router = routers.SimpleRouter()
router = routers.DefaultRouter()
# -->> получения индитификатора роутера адресс http://127.0.0.1:8000/api/v1/
print(router.urls)
# name = women-list,women 'women its aur model,basename  обязателен если нету queryset
router.register(r'women', WomenViewSet,basename='women')
# router.register(r'readwomen',WomenReadonlySet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/womenlist/', WomenAPIlist.as_view()),
    # path('api/v1/womenlist/<int:pk>/',WomenUPdateAPIWiew.as_view()),
    # path('api/v1/womendetail/<int:pk>/',WomenAPIDetailView.as_view())
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womendetail/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
]
