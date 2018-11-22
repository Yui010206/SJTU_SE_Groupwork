from django.conf.urls import patterns, include, url

urlpatterns = patterns('trade.views',
        url(r'^goodsList', 'goodsList'),
        url(r'^goodsPurchase', 'goodsPurchase'),
        url(r'^buyHis', 'buyHis'),
)
