from django.urls create path

from . import views

urlpatterns = [
path('',views.home, name='Index'),
path('capture/', views.capture,name="capture"),
]
