from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='success'),
    url(r'^add$', views.create, name='create'),
    url(r'^book/(?P<id>\d+)$', views.review, name='review-book'),

    ]
