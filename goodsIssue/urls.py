from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('goodsIssue.views',
        url(r'^release/$','release'),
        url(r'^market/$','market'),

        url(r'(?P<good_id>\d+)/$','detail'),
        url(r'^buyhis/$','purchaseHistory'),
        url(r'^search/$','search')

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
