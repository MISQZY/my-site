from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>', ViewNews.as_view(), name='view_news')
    # path('category/<int:category_id>/', get_category, name='category'),
    # path('news/<int:news_id>', view_news, name='view_news'),
    # # path('', index, name='home'),
]
