"""djangonautic URL Configuration

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

#meu path é o url dele
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#let us append to the URL pattern so that Django can handle the serving goal

urlpatterns = [
    path('admin/', admin.site.urls),
    #adicionei a página about + indiquei a função que será executada quando alguém
    #pedir a rota about
    path('about/', views.about),
    #adicionei a home page
    path('', views.homepage),
    #o include vai fazer com que o Django olhe dentro do urls.py do articles app
    path('articles/', include('articles.urls')),
]

urlpatterns += staticfiles_urlpatterns()
#check if we are in debug mode, then append here to serve the static file