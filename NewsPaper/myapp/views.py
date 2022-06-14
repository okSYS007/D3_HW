# from django.shortcuts import render
from django.views.generic import ListView, DetailView # импортируем класс получения деталей объекта
from .models import Post
from datetime import datetime
 
class PostList(ListView):
    model = Post  
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-creation_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow() # добавим переменную текущей даты time_now
        return context
 
# # создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'article.html' # название шаблона будет product.html
    context_object_name = 'article' # название объекта
    queryset = Post.objects.filter(post_choice = 1).order_by('-creation_date')
    