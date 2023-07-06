from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import CommentForm, ArticleForm
from blog.models import Article, Tag, Category
# Create your views here.

def get_page_articles(request, articles, pages_num):
    paginator = Paginator(articles, pages_num)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)

def blog(request):
    if not request.user.is_authenticated:
        return render(request, 'blog/error_login.html', {'title': "Access error"})
    articles = sorted(Article.objects.filter(status='active'), key=lambda article: article.updated_at, reverse=True)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/articles.html', {'page_articles': get_page_articles(request, articles, 4), 'tags' : tags, 'categories': categories})

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
    return render(request, 'blog/articles_filter.html', {'page_articles': get_page_articles(request, articles), 'title': tag, 'tags' : tags, 'filter': 'tag', 'categories': categories})

@login_required()
def articles_category_list(request, category):
    articles = Article.objects.filter(category__slug=category, status='active')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/articles_filter.html', {'page_articles': get_page_articles(request, articles, 3), 'title': category, 'tags' : tags, 'filter': 'category', 'categories': categories})

@login_required()
def search(request):
    query = request.GET.get('query', '')
    articles = Article.objects.filter(Q(title__icontains=query) | Q(text__icontains=query) | Q(discription__icontains=query))
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/search.html', {'page_articles': get_page_articles(request, articles, 3), 'title': 'Search through blog', 'query': query, 'tags' : tags, 'categories': categories})

@login_required()
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.add_message(request, messages.INFO, 'Article created')
            return redirect('details', slug=article.slug)
    else:
        form = ArticleForm()
    
    return render(request, 'blog/create.html', {'form': form, 'title' : 'Article creation'})

@login_required()
def update(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        
        if form.is_valid():
            article = form.save()
            messages.add_message(request, messages.INFO, 'Article updated')
            return redirect('details', slug=article.slug)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/update.html', {'form': form, 'title': 'Article edit'})

@login_required()
def delete(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    article.delete()
    messages.add_message(request, messages.INFO, 'Article deleted')
    return redirect('blog')