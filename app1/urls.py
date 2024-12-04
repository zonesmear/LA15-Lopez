from django.urls import path
from . import views

#url configuration
urlpatterns = [
    path('Hello/', views.say_hello),
    path('hi/', views.say_hi),
    path('posts/', views.blog_list),
    path('posts/<id>/', views.blog_detail),
  
      
]