from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from blog.models import Article
# Create your views here.
def blog(request):
    articles = sorted(Article.objects.all(), key=lambda article: article.updated_at, reverse=True)
    return render(request, 'blog/articles.html', {'articles': articles})

def details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return  redirect('details', slug=slug)
    else:
        form = CommentForm()
    
    return render(request, 'blog/details.html', {'article': article, 'form': form})

def articles_tag_list(request, tag):
    articles = Article.objects.filter(tags__slug=tag)
    return render(request, 'blog/articles_tag.html', {'articles': articles, 'title': tag})

def search(request):
    query = request.GET.get('query', '')
    articles = Article.objects.filter(Q(title__icontains=query) | Q(text__icontains=query) | Q(discription__icontains=query))
    
    return render(request, 'blog/search.html', {'articles': articles, 'title': 'Search through blog', 'query': query})