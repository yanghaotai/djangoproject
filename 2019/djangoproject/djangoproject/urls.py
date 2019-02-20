"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from loan import views,views1
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index/$', views.index), #添加index/路径配置
    # url(r'^login_action/$', views.login_action),
    # url(r'^event_manage/$', views.event_manage),
    # url(r'^accounts/login/$', views.index),
    url(r'^loan/$', views.loan),
    url(r'^loan_action/$', views.loan_action),
    url(r'^idcard/$', views.idcard),
    url(r'^idcard_action/$', views.idcard_action),
    url(r'^ifidcard/$', views.ifidcard),
    url(r'^ifidcard_action/$', views.ifidcard_action),
    url(r'^jiami/$', views.jiami),
    url(r'^jiami_action/$', views.jiami_action),
    url(r'^snake/$', views.snake),
    url(r'^snake_action/$', views.snake_action),
    url(r'^pizza/$', views1.pizza),
    url(r'^pizza_action/$', views1.pizza_action),
]
