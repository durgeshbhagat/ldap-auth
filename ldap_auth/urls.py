from django.conf.urls import url
from django.contrib import admin
from ldap_auth import views
app_name = 'ldap_auth'

urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login'),
]