"""Routes of the project"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('accounts/', include('accounts.urls')),
    path('user/', include('user.urls')),

    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]

urlpatterns += static(
    settings.IMAGES_RELATIVE_PATH,
    document_root=settings.IMAGES_ROOT
)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
