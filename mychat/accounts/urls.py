from tempfile import template
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', views.profile, name='profile'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name ="password_reset_form.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<tocken>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
  
  ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)