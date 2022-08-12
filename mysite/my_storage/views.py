from django.core.files import File
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Storage, Category
import docx2txt

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'my_storage/categories_list.html'
    context_object_name = 'categories'
    select_related = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards'] = Storage
        context['title'] = 'Список категорий'
        return context


class GetCard(LoginRequiredMixin, DetailView):
    model = Storage
    pk_url_kwarg = 'card_id'
    template_name = 'my_storage/card_view.html'
    context_object_name = 'card'
    select_related = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file_content'] = get_file_content(Storage.objects.get(pk=self.kwargs['card_id']))
        return context

@login_required
def get_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    cards = Storage.objects.filter(category_id=category_id, is_published=True).order_by('title', 'created_at')

    return render(request, 'my_storage/cards.html', {'category': category, 'cards': cards})


def get_file_content(card):
    if str(card.file.path).endswith(".py"):
        f = open(card.file.path, mode='rb')
        file_content = str(File(f).read()).replace('\\n', '<br>').replace('\\r', '').replace('\\\\', '\\')
        file_content = file_content[2:-1]
        return file_content
    elif str(card.file.path).endswith(".docx"):
        file_content = docx2txt.process(f"{card.file.path}")
        return file_content
    else:
        file_content = 'НЕ удалось отобразить содержимое файла'
        return file_content



# def categories_list(request):
#     categories = Category.objects.all()
#     cards = Storage.objects.all()
#     context = {
#         'categories': categories,
#         'cards': cards,
#         'title': 'Список категорий',
#     }
#     return render(request, 'my_storage/categories_list.html', context)


# def get_card(request, card_id):
#     card = Storage.objects.get(pk=card_id)
#     if str(card.file.path).endswith(".py"):
#         f = open(card.file.path, mode='rb')
#         file_content = str(File(f).read()).replace('\\n', '<br>').replace('\\r', '').replace('\\\\', '\\')
#         file_content = file_content[2:-1]
#     elif str(card.file.path).endswith(".docx"):
#         file_content = docx2txt.process(f"{card.file.path}")
#     return render(request, 'my_storage/card_view.html', {'card': card, 'file_content': file_content})

# class GetCategory(DetailView):
#     model = Storage
#     pk_url_kwarg = 'category_id'
#     template_name = 'my_storage/cards.html'
#     context_object_name = 'category'
#     select_related = 'category'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cards'] = Storage.objects.filter(category_id = self.kwargs['category_id'], is_published=True).order_by('title', 'created_at')
#         return context
