from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),  # 'restaurant/' 경로로 접근
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
