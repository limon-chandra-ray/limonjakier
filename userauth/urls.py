from django.urls import path
from userauth import views
from userauth.views import RegisterView,LogInView
urlpatterns = [
    path('register',RegisterView.as_view(),name='register'),
    path('login',LogInView.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
]
