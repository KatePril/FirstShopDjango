from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from blog.models import Article, Tag
# Create your views here.
def blog(request):
    articles = sorted(Article.objects.filter(status='active'), key=lambda article: article.updated_at, reverse=True)
    return render(request, 'blog/articles.html', {'articles': articles, 'tags' : tags})

def details(request, slug):
    article = get_object_or_404(Article, slug=slug, status='active')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return  redirect('details', slug=slug)
    else:
        form = CommentForm()
    tags = Tag.objects.all()
    return render(request, 'blog/details.html', {'article': article, 'form': form, 'tags' : tags})

def articles_tag_list(request, tag):
    articles = Article.objects.filter(tags__slug=tag, status='active')
    tags = Tag.objects.all()
    return render(request, 'blog/articles_tag.html', {'articles': articles, 'title': tag, 'tags' : tags})

def search(request):
    query = request.GET.get('query', '')
    articles = Article.objects.filter(Q(title__icontains=query) | Q(text__icontains=query) | Q(discription__icontains=query))
    tags = Tag.objects.all()
    return render(request, 'blog/search.html', {'articles': articles, 'title': 'Search through blog', 'query': query, 'tags' : tags})