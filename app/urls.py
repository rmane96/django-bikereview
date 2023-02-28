from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('bike/',include('bike.urls')),
    path('user/',include('user.urls')),
    path('api-token-auth/', auth_views.obtain_auth_token)
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()