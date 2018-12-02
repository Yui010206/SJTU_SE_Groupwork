from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'dtiaozao.view.index'),
    url(r'^search/', 'dtiaozao.view.search'),
    url(r'^goodsIssue/', include('goodsIssue.urls')),
    url(r'^trade/', include('trade.urls')),
    url(r'^account/',include('account.urls'))
)+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)
