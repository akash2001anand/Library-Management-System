from django.urls import path
from . import views
from .views import CustomLoginView
urlpatterns=[
    path('', views.index, name='index'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('user_login/', views.user_login, name='user_login'),
    path('admin_auth/', CustomLoginView.as_view(), name='admin_auth'),
    path('admin_home/', views.admin_home, name='admin_home'),
]