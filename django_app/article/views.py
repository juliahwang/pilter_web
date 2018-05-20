from django.shortcuts import render

# Create your views here.
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(
        request,
        'article/articles.html',
        context=context
    )
