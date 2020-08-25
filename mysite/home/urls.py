from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('contact', views.contact_form, name='contact'),
    path('login', views.login_form),
    path('logout', views.log_out),
    path('addcomment/<int:proid>', views.comment_add, name='addcomment'),
    path('deletecomment/<int:id>', views.comment_delete, name='deletecomment'),
    path('comments', views.comment_list, name='comments'),
    path('category/<int:catid>/', views.category),

]
