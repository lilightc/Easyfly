"""csc3170 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path ##re_path新增
from django.conf.urls import url
from file import views
from django.views import static ##新增
from django.conf import settings ##新增
from django.conf.urls import url ##新增

# 网址注册
# 若想通过外网访问(laxdata域名)，请加前缀/hello/ （如/hello/new_feature/）
# uwsgi同步后即可看到效果

# 如果想在html中通过<href>引用static中的静态文件，请按如下步骤操作：
# 1、将css/jpg等静态文件放置在/static/中
# 2、运行python3 manage.py collectstatic，Django会自动将/static/的文件转移到/staticfile/中（手动操作无效）
# 3、在html中已<src = ../static/xxx.jpg> 或 <href = ..static/xxx.css>方式引用静态文件

urlpatterns = [
    path('hello/admin/', admin.site.urls),
    path('hello/', views.hello),       # 每当访问/hello/时，就会执行/file/views/中 def hello(request)这一函数
    path('hello2/', views.hello2),
    path('hello/test_db/',views.test_Fetch_Db),
    path('hello/login_temp/', views.login_temp), 
    path('hello/signUp/', views.signUp), # TODO
    path('hello/signUp_page/', views.signUp_page), # TODO
    path('hello/search_page/', views.search_page),
    path('hello/search_result/', views.search_result),
    path('hello/user/', views.user),
    path('hello/logout/', views.logout),
    path('hello/testpage/', views.airlineJump),

    path('hello/prediction/', views.prediction), #后端 TODO

    # 404有可能是因为这里没写完，且未comment掉，导致全域无法访问
    path('hello/test/', views.test), ##路由测试 #DONE
    re_path(r"^hello/testjump/$", views.testjump, name='testjump'), #路由test   #DONE
    
    url(r'^hello/airport/$', views.airport, name='airport'),
    url(r'^hello/aircraft/$', views.aircraft, name='aircraft'),
    url(r'^hello/airline/$', views.airline, name='airline'),

    #拼接跳转地址
    url(r'^hello/airportJump/(.*)/$', views.airportJump, name='airportJump'),
    url(r'^hello/aircraftJump/(.*)/$', views.aircraftJump, name='aircraftJump'),
    url(r'^hello/airlineJump/(.*)/$', views.airlineJump, name='airlineJump'),
    


    url(r'^hello/static/(?P<path>.*)$', static.serve,       # 加载static界面!!
      {'document_root': settings.STATIC_ROOT}, name='static'),
    ]
