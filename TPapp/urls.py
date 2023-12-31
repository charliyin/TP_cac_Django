from django.urls import path
from .views import index, contacto, remuneraciones, personal, exit
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',index, name="index"),
    path('contacto/',contacto, name="contacto"),
    path('personal/',personal, name="personal"),
    path('remuneraciones/',remuneraciones, name="remuneraciones"),
    path('logout/',exit, name="exit"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)