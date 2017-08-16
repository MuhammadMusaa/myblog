from article.views import hello_word
from django.conf.urls import url
from article import views

urlpatterns = [
    url(r'^hello_dunia/$', hello_word),
    url(r'^nama/(?P<nama_saya>[\w-]+)/(?P<umur>[0-9]+)$', views.nama_saya),
    ]