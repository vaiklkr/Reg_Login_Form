
from django.contrib import admin
from django.urls import path, re_path
from RegAndLoginApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', views.home),
    re_path('^register$', views.register),
    re_path('^login$', views.login),
]
