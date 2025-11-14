from django.urls import path
from django.contrib import admin
from bookmark import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
