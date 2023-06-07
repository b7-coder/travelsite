from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from travel_site.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('blog/', blog),
    path('contact/', contact),
    path('services/', service),
]

urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)