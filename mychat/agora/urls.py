from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('video/', views.video, name='agora-index'),
    path('pusher/auth/', views.pusher_auth, name='agora-pusher-auth'),
    path('token/', views.generate_agora_token, name='agora-token'),
    path('call-user/', views.call_user, name='agora-call-user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)