from django.conf.urls import patterns, include, url

urlpatterns = patterns('trade.views',
        url(r'^goodsList', 'goodsList'),
        url(r'^goodsPurchase', 'goodsPurchase'),
        url(r'^buyHistory', 'buyHistory'),
        url(r'^saleHistory','saleHistory'),
        url(r'(?P<good_id>\d)/$','detail')
)
