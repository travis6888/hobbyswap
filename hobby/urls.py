from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hobbyswap.views.home', name='home'),
    url(r'^user/$', 'hobbyswap.views.user', name='user'),
    url(r'^contact/$', 'hobbyswap.views.contact', name='contact'),
    url(r'^careers/$', 'hobbyswap.views.careers', name='careers'),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^error/$', 'hobbyswap.views.error', name='error'),
    url(r'^create_review/(?P<item_id>\d+)/$', 'hobbyswap.views.create_review', name='create_review'),
    url(r'^view_review/(?P<item_id>\d+)/$', 'hobbyswap.views.view_review', name='view_review'),
    url(r'^edit_review/(?P<item_id>\d+)/$', 'hobbyswap.views.edit_review', name='edit_review'),
    url(r'^post/$', 'hobbyswap.views.post_item', name='post_item'),
    url(r'^edit_post/(?P<item_id>\d+)/$', 'hobbyswap.views.edit_post', name='edit_post'),
    url(r'^listing/$', 'hobbyswap.views.listing', name='listing'),
    url(r'^reviews/$', 'hobbyswap.views.reviews', name='reviews'),
    url(r'^view_listing/(?P<item_id>\d+)/$', 'hobbyswap.views.view_listing', name='view_listing'),
    url(r'^about/$', 'hobbyswap.views.about', name='about'),
    url(r'^category/$', 'hobbyswap.views.category', name='category'),
    url(r'^thanks/$', 'hobbyswap.views.thanks', name='thanks'),
    url(r'^view_user/(?P<user_id>\d+)/$', 'hobbyswap.views.view_user', name='view_user'),
    url(r'^edit_user/(?P<user_id>\d+)/$', 'hobbyswap.views.edit_profile', name='edit_user'),
    url(r'^profile/$', 'hobbyswap.views.profile', name='profile'),
    url(r'^register/$', 'hobbyswap.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)