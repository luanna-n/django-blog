from django.contrib import admin
from .models import Article
#pegue o models file e importe a classe Article

# Register your models here.
admin.site.register(Article)
#fazer o Article aparecer na area do admin