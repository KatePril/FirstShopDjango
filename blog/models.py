from django.db import models

# Create your models here.
class Article(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='articles', default=1, verbose_name='Category')
    tags = models.ManyToManyField('Tag', related_name='articles', verbose_name='Tags')
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(verbose_name='URL', unique=True)
    discription = models.TextField(verbose_name='Article discription')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created on')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated on')
    
    def __str__(self):
        return f'{self.title}'
    
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category name')
    slug = models.SlugField(verbose_name='URL', default='', unique=True)
    
    def __str__(self):
        return f'{self.name}'

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Tag name', unique=True)
    slug = models.SlugField(verbose_name='URL', default='', unique=True)

    def __str__(self):
        return f'{self.name}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255, verbose_name='User name')
    email = models.EmailField(verbose_name='Email')
    content = models.TextField(verbose_name='Comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created on')

    def __str__(self):
        return f'{self.article.title} - {self.content}'