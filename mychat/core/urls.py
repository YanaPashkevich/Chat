from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('main/', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up')

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
