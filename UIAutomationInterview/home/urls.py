from django.urls import path, include
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.make_payment, name='pay'),
    path('', auth_views.LogoutView.as_view(), name='logout'),
]