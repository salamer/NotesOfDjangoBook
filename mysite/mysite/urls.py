from django.conf.urls import *
from django.contrib import admin
from books.models import Book
from blog.models import blog
from mysite import sendMailViewByForms

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

##urlpatterns += patterns('mysite.sendMailViewByForms',
##    url(r'^contact/$','contact'),
##    url(r'^contact/thanks/$','contact_thanks'),                  
##)

urlpatterns += patterns('',
    url(r'^contact/$',sendMailViewByForms.method_splitter, \
        {'GET_method':sendMailViewByForms.get_contact, \
         'POST_method':sendMailViewByForms.post_contact}),
    url(r'^contact/thanks/$',sendMailViewByForms.contact_thanks),                  
)

urlpatterns += patterns('mysite.views',
    url(r'^hello/$','hello'),
    url(r'^time/$','current_datetime'),
    url(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    url(r'^search/$','show_search_result'),
    url(r'^request-info/$','show_request'),
    url(r'^search-form/$','search_form'),
)

urlpatterns += patterns('mysite.articlesViews',
    (r'^chapter8_url_view/name_groups/articles/(?P<year>\d{4})/$', 'year_archive'),
    (r'^chapter8_url_view/name_groups/articles/(?P<year>\d{4})/(?P<month>\d{2})/$','month_archive'),
    url(r'^chapter8_url_view/fake_captured_URLconf_values/articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$','day_archive'),
    url(r'^chapter8_url_view/fake_captured_URLconf_values/articles/birthday/$','day_archive',{'year':'2014','month':'09','day':'16'}),
)

urlpatterns += patterns('mysite.foobar_view',
    (r'^chapter8_url_view/pass_extra_options_to_view/foo/$', \
     'foo_bar_view',{'template_name':'foobar/foo.html','search_str':'world'}),
    (r'^chapter8_url_view/pass_extra_options_to_view/bar/$', \
     'foo_bar_view',{'template_name':'foobar/bar.html','search_str':'the'}),
)

urlpatterns += patterns('mysite.objectView',
    url(r'^chapter8_url_view/make_a_view_generic/blog/$','object_list',{'model':blog}),
    url(r'^chapter8_url_view/make_a_view_generic/book/$','object_list',{'model':Book}),
)

urlpatterns += patterns('mysite.blogPageView',
    url(r'^chapter8_url_view/use_default_view_arguments/blog/$','show_blog_page'),
    url(r'^chapter8_url_view/use_default_view_arguments/blog/page(?P<num>\d+)/$','show_blog_page'),
)
