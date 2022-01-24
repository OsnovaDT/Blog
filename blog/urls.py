"""Routes of the project"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('accounts/', include('accounts.urls')),
    path('user/', include('user.urls')),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),

    # API token
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'api/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
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
