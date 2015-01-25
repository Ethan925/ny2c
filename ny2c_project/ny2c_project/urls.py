from django.conf.urls import patterns, include, url
from django.contrib import admin
from ny2c_app import views

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'ny2c_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomeView.as_view(), name='home'),

)

