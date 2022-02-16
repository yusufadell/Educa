from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseListView
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('', CourseListView.as_view(), name='course_list'),
    path('students/', include('students.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('openapi', get_schema_view(  # new
        title="Educa API",
        description="Api For Enrolling in Courses.",
        version="1.0.0"
    ), name='openapi-schema'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
