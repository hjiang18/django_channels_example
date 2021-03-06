from django.conf.urls import url
from userlist.views import user_list, signin, signout, singup

app_name='userlist'
urlpatterns = [
    url(r'^$', user_list, name='user_list'),
    url(r'^login/$'  , signin , name='login'),
    url(r'^signin/$' , signin , name='signin'),
    url(r'^logout/$' , signout, name='logout'),
    url(r'^signout/$', signout, name='signout'),
    url(r'^singup/$' , singup , name='singup'),
]
