
from django.contrib import admin
from django.urls import path
from accounts import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.Registration.as_view(),name='register'),
    path('login/',views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('userslist/',views.UserListView.as_view(),name='userslist'),
    path('doctorlist/',views.UserDoctorView.as_view(),name = 'doctorlist'),
    path('userprofile/',views.UserProfileView.as_view(),name = 'profile'),
    path('adminuserlist/',views.AdminViewUsers.as_view(),name='adminuserlist'),
    path('adminuserlist/<int:pk>/',views.AdminViewUsers.as_view(),name='user-detail'),
    path('hello/',views.hello_world,name='hello'),
] 
