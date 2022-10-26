
from django.contrib import admin
from django.urls import path, include

from asosiy.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()
router.register('aktyorlar', AktyorViewSet)
router.register('kinolar', KinoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token_olish/', TokenObtainPairView.as_view()),
    path('token_yangilash/', TokenRefreshView.as_view()),
    path('token_ber/', obtain_auth_token ),
    path('kinolar/', HammaKinolar.as_view() ),
    path('kinolar/<int:pk/', KinoGetDeleteUpdete.as_view() ),
    path('aktyorlar/', HammaAktyorlar.as_view() ),
    path('aktyorlar/<int:pk/', AktyorGetDeleteUpdete.as_view() ),
    path('', include(router.urls)),
    # path('aktyorlar/', HammaAktyorlarAPI.as_view()),
    # path('kinolar/', HammaKinolarAPI.as_view()),
    # path('kino/<int:pk>/', KinoAPI.as_view()),
    # path('aktyor/<int:pk>/', AktyorAPI.as_view()),

]
