from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('login/', views.login, name='Login'),
    path('todo/', views.todo, name='Todo'),
    path('todo/edit/<int:srno>/', views.edit_todo, name='edit_todo'),  # Edit URL
    path('todo/delete/<int:srno>/', views.delete_todo, name='delete_todo'),  # Delete URL
    # path('todo/', views.todo, name='Todo'),

]


