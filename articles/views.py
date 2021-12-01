from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article
#importar o Article para exibir os objs => articles

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    #coleta todos os obj da table Article + organiza por data (.order_by('forma de organizar'))
    #usando o .models (ORM)!!!
    return render(request, 'articles/article_list.html', {
        'articles': articles
    })
    #add a 3º parameter to the render function
    #the data is what will be sent to the view or the template(!)
    #é um dict que será enviado ao template (html file) com o que acabou
    #de ser recebido em articles na linha 7

    #vou renderizar esses artigos aqui da view,
    #que foram buscados lá da DB da models
    #lá pra article_list.html

def article_detail(request, slug):
    # return HttpResponse(slug)
    #captura para onde o user quer ir e joga dentro da função
    #e retorna na tela o slug pro user ver

    #query the data base e get a ARTICLE TO OUTPUT
    article = Article.objects.get(slug=slug)
    #the slug paramenter has to be equal the slug we get here
    return render(request, 'articles/article_detail.html', { 'article': article})
    #1º request, 2º template to render, 3º dados (dict) // prop = o article da var
