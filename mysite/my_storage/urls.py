from django.urls import path

from .views import *

urlpatterns = [
    path('', CategoryList.as_view(), name = 'categories_list'),
    # path('<int:category_id>/', GetCategory.as_view(), name = 'categories_list_for_get'),
    path('cards/<int:card_id>/', GetCard.as_view(), name = 'card_id'),
    # path('cards/<int:card_id>/', get_card, name = 'card_id')
    # path('', categories_list, name = 'categories_list'),
    path('<int:category_id>/', get_category, name = 'categories_list_for_get'),
]
