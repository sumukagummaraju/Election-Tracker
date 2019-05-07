"""ET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers

from ET_App.views import UserViewSet, QuestionsViewSet, OptionViewSet

# router = routers.DefaultRouter()
# router.register('user', UserViewSet)
# router.register('questions', QuestionViewSet)
# router.register('user', UserViewSet)
# router.register('user', UserViewSet)

router1 = routers.DefaultRouter()
router1.register('user', UserViewSet)
router2 = routers.SimpleRouter()
router2.register('questions', QuestionsViewSet)
router3 = routers.SimpleRouter()
router3.register('options',OptionViewSet)
# router4 = routers.SimpleRouter()
# router.register('userselectedoption',UserSelectedOptionViewSet)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/',include(router1.urls)),
    path('api/', include(router2.urls)),
    path('api/', include(router3.urls)),
    # path('api/', include(router.urls))
]
