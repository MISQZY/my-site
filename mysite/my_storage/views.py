from django.core.files import File
from django.shortcuts import render
from django.views import generic


from .models import Storage, Category
import docx2txt

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class CategoryList(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = 'my_storage/categories_list.html'
    context_object_name = 'categories'
    select_related = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards'] = Storage
        context['title'] = 'Список категорий'
        return context

def acess_level_check(user):
    return user.acess_level >= 1

class GetCard(LoginRequiredMixin, generic.DetailView):
    model = Storage
    pk_url_kwarg = 'card_id'
    template_name = 'my_storage/card_view.html'
    context_object_name = 'card'
    select_related = 'category'

    def test_func(self):
        return self.request.user.acess_level >= Storage.objects.get(pk=self.kwargs['card_id']).acess_required

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
