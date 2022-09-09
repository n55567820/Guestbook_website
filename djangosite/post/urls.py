from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:a_id>', views.view_article, name='view_article'),
    path('articles/create', views.create_article, name='create_article'),
    path('articles/edit/<int:a_id>', views.edit_article, name='edit_article'),
    path('articles/delete/<int:a_id>', views.delete_article, name='delete_article'),
    path('articles/<int:a_id>/new_comment', views.new_comment, name='new_comment'),
    path('articles/<int:a_id>/edit_comment/<int:c_id>', views.edit_comment, name='edit_comment'),
    path('articles/<int:a_id>/del_comment/<int:c_id>', views.del_comment, name='del_comment'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]