from django.conf import settings
from django.urls import include, path

from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import IsAuthenticatedOrReadOnly

urlpatterns = [
    path(
        'v1/',
        include('oo.api.v1.urls')
    ),
    path('docs/',
        include_docs_urls(
            title='Infinity API',
            permission_classes=(IsAuthenticatedOrReadOnly,)
        )
    ),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]
