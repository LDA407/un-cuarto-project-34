

from django.conf import settings
from django.conf.urls.static import static, serve
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    re_path(r'^un_cuarto_administrator_site/', admin.site.urls),
    # re_path(r'^$', include('un_cuarto.urls', namespace='un_cuarto')),
    # path('un_cuarto_administrator_site/', admin.site.urls),
    path('', include('un_cuarto.urls', namespace='un_cuarto')),
] += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += [
#     re_path(r'^static/(?P<path>.*)$', serve,{
#         "document_root" : settings.STATIC_ROOT
#     }),
#     re_path(r'^media/(?P<path>.*)$', serve,{
#         "document_root" : settings.MEDIA_ROOT
#     })
# ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
