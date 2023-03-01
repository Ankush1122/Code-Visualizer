from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('execute', views.execute_code, name='execute_code')
]
