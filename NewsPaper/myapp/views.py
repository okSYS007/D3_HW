# from django.shortcuts import render
from django.views.generic import ListView, DetailView # импортируем класс получения деталей объекта
from .models import Post
 
 
class PostList(ListView):
    model = Post  
    template_name = 'news.html'
    context_object_name = 'news'
 
 
# # создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'news.html' # название шаблона будет product.html
    context_object_name = 'news' # название объекта