from django.urls import path
from api.v1.notify import views


urlpatterns = [
    path('', views.notify, name='notify'),
]