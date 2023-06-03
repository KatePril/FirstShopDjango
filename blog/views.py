from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from blog.models import Article
# Create your views here.
def blog(request):
    articles = sorted(Article.objects.all(), key=lambda article: article.updated_at, reverse=True)
    return render(request, 'blog/articles.html', {'articles': articles})

def details(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return  redirect('details', id=id)
    else:
        form = CommentForm()
    
    return render(request, 'blog/details.html', {'article': article, 'form': form})