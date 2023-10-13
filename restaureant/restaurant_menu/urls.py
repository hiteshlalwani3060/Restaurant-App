from django.urls import path
from . import views
urlpatterns= [
    path('', views.MenuList.as_view(), name="home"),
    path('item/<int:pk>/', views.MenuItemDetails.as_view(), name="menu_item"),
    path('item/about', views.about, name='about')
]

# item/<int:pk> syntax of the django to handle dynamic urls