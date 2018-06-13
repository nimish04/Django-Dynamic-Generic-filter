from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from core import views as core_views


urlpatterns = [
	path('admin/', admin.site.urls),
	url(r'^package/', include('core.urls')),
    url(r'^$', core_views.home, name='home'),
    # url(r'^login/$', core_views.signup, name='login'),
	url(r'login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),

    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
    url(r'^forgot/$', core_views.forgot, name='forgot'),
    url(r'^change/$', core_views.change, name='change'),

]
