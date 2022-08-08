from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Recommendation/', include('django.contrib.auth.urls')),
    # for reset password
    path('', include('Recommendation.urls'))
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
