from django.shortcuts import render, get_object_or_404

from blog.models import Article
# Create your views here.
def blog(request):
    articles = sorted(Article.objects.all(), key=lambda article: article.updated_at, reverse=True)
    return render(request, 'blog/articles.html', {'articles': articles})

def details(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/details.html', {'article': article})