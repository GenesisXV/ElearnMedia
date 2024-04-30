from django.urls import path
from . import views
app_name = 'micromedia'

urlpatterns = [
    path('', views.elearn, name='elearn')
]