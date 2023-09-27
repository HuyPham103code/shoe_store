from django.urls import path
from . import views

urlpatterns = [
    path('wife', views.wife, name='wife'),
    path('', views.home, name='home'),
    path('search/', views.search_category, name='search_category'),
    path('category/<str:category>/', views.show_category, name='show_category'),
    path('shoe/<int:id>/', views.show_shoe, name='show_shoe'),
]