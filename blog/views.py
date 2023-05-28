from django.shortcuts import render, get_object_or_404

from blog.models import Article
# Create your views here.
def blog(request):
    articles = Article.objects.all()
    return render(request, 'blog/articles.html', {'articles': articles})

def details(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/details.html', {'article': article})