from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^signUp/$', views.sign_up, name='signUp'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^products/$', views.products, name='products'),

)

