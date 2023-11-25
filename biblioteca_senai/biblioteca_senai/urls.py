from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('site_biblioteca.urls')),
    path('social-auth/', include('social_django.urls', namespace='social-auth')),
]

urlpatterns += staticfiles_urlpatterns()
