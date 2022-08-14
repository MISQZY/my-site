from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name= 'news'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('id/<int:news_id>', ViewNews.as_view(), name='view_news')
]
