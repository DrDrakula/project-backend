from django.conf import settings
from django.views.generic import RedirectView
from django.urls import path, include


urlpatterns = [
    path('', RedirectView.as_view(pattern_name="api-root", permanent=True)),
    path('api/v1/', include('apps.api.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns