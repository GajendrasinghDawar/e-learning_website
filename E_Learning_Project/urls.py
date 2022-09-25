from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .auth import loginView
from courses.views import CourseListView

urlpatterns = [
    path('accounts/login/', loginView.MyloginView.as_view(),  name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),
         name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('', CourseListView.as_view(), name='course_list'),
    path('dashboard/', CourseListView.as_view(), name='dashboard'),
    path('students/', include('students.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('chat/', include('chat.urls', namespace='chat')),
]
