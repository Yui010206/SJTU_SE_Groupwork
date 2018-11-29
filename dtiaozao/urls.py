from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'dtiaozao.view.index'),
    url(r'^search/', 'dtiaozao.view.search'),
    url(r'^goodsIssue/', include('goodsIssue.urls')),
    url(r'^trade/', include('trade.urls')),
    url(r'^account/',include('account.urls'))
)
