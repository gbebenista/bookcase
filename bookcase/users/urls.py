from django.contrib.auth import views
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from .views import RegisterView, ViewLogin

urlpatterns = [
    path('signup', RegisterView.as_view(), name='register'),
    path('', ViewLogin.as_view(), name='login'),
    path('password-reset/', views.PasswordResetView.as_view(), name="password_reset"),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout', LogoutView.as_view(), name='logout')
]

