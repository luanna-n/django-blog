from django.db import models
from django.db.models.fields import CharField
from django.urls.converters import SlugConverter

# Create your models here.

class Article(models.Model):
    #porque models? porque os tipos estão DENTRO dela
    #estou acessando por notação de ponto
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #add in thumbnail later
    #add in author later

    #como o obj vai aparecer no admin ou no shell
    def __str__(self):
        return self.title
    #<QuerySet [<Article: Article object (1)>]>
    #<QuerySet [<Article: article title str name>]>

    def snippet(self):
        return self.body[:50] + '...'