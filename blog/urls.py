"""blog URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from myblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_page),
    #path('blog/', include('blog.urls'))大项目还有多个APP时可以这样做，
    # 要在blog目录下建一个urls.py文件，并且需要导入from django.urls import include, path
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
