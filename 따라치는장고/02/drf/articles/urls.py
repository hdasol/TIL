from django.urls import path, include
from . import views

urlpatterns = [
    # CRUD
    # create
    path('articles/', views.article_list),
    # update, delete, read
    path('articles/<int:pk>', views.article_detail),
]
