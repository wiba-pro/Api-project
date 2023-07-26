from django.urls import path, include
from . import views
from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token
urlpatterns=[
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('students/', views.StudentApiView.as_view(), name='Students'),
    # path("user/", views.createNewUser.as_view(), name='user'),
    path('auth/', include('djoser.urls')),
     path('auth/', include('djoser.urls.authtoken')),
    # path("token_login/", obtain_auth_token, name="token_code"),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='Student'),
    path('course/<int:pk>/', views.CourseDetail.as_view(), name='course'),
    path('teachers/', views.TeacherListView.as_view(), name='Teacher'),

]