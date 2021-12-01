from django.urls import path
from . import views

app_name = 'articles'
#name space the file
#ajuda o django a saber onde está o 'name' que eu quero que ele encontre

urlpatterns = [
    #adicionei a página lista de artigos + indiquei a função que será executada quando alguém
    #pedir a rota da lista de artigos
    #minhas URLS são nomeadas pra not hard code the url in href
    path('', views.article_list, name='list'),
    path('<slug:slug>/', views.article_detail, name='detail'),
    #<slug:slug> is a name capturing group (2º slug poderia ser qualquer outro nome)
    #1º slug is type of the parameter
    #2º slug is the name of the parameter
]
