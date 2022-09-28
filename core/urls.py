from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('furnapp.urls')),
    path("dashboard/", include('dashboard.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + i18n_patterns(
    path('i18n/', include("django.conf.urls.i18n")),
    prefix_default_language = False
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
