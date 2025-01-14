#school_management_drf/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),  # Incluindo as URLs do app students
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('courses.urls')),
    path('api/', include('teachers.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
