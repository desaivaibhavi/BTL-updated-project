from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^update/$', views.update, name='update'),
	url(r'^post_new/$', views.post_new, name='post_new'),
	url(r'^view_post/$', views.view_post, name='view_post'),
	url(r'^edit_post/$', views.edit_post, name='edit_post'),
    url(r'^edit_post_page/$', views.edit_post_page, name='edit_post_page'),



]