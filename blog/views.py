from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import CommentForm
from blog.models import Article, Tag, Category
# Create your views here.

def blog(request):
    if not request.user.is_authenticated:
        return render(request, 'blog/error_login.html', {'title': "Access error"})
    articles = sorted(Article.objects.filter(status='active'), key=lambda article: article.updated_at, reverse=True)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/articles.html', {'articles': articles, 'tags' : tags, 'categories': categories})

@login_required()
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
    categories = Category.objects.all()
    return render(request, 'blog/details.html', {'article': article, 'form': form, 'tags' : tags, 'categories': categories})

@login_required()
def articles_tag_list(request, tag):
    articles = Article.objects.filter(tags__slug=tag, status='active')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/articles_filter.html', {'articles': articles, 'title': tag, 'tags' : tags, 'filter': 'tag', 'categories': categories})

@login_required()
def articles_category_list(request, category):
    articles = Article.objects.filter(category__slug=category, status='active')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/articles_filter.html', {'articles': articles, 'title': category, 'tags' : tags, 'filter': 'category', 'categories': categories})

@login_required()
def search(request):
    query = request.GET.get('query', '')
    articles = Article.objects.filter(Q(title__icontains=query) | Q(text__icontains=query) | Q(discription__icontains=query))
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/search.html', {'articles': articles, 'title': 'Search through blog', 'query': query, 'tags' : tags, 'categories': categories})