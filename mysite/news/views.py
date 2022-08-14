from django.views import generic


from .models import News, Category

class HomeNews(generic.ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список новостей'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')



class NewsByCategory(generic.ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id']).select_related('category')


class ViewNews(generic.DetailView):
    model = News
    pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'
    template_name = 'news/view_news.html'
    allow_empty = False
