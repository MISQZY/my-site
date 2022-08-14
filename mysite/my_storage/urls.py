from django.urls import path

from .views import *

urlpatterns = [
    path('', CategoryList.as_view(), name = 'categories_list'),
    path('cards/<int:card_id>/', GetCard.as_view(), name = 'card_id'),
    path('category/<int:category_id>/', get_category, name = 'categories_list_for_get'),
]
