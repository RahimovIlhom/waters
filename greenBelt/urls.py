from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from main.views import *

schema_view = get_schema_view(
   openapi.Info(
      title="Yer sug'orish texnikasi va xizmatlari",
      default_version='v1',
      description="O'quv maqsadlarida foydalanish uchun",
      contact=openapi.Contact(email="<frjavohir@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('menyular', MenyuViewSet)
router.register('home', HomeViewSet)
router.register('submenyular', SubMenyuViewSet)
router.register('mahsulotlar', MahsulotViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



