from .views import *
from django.urls import path




urlpatterns =[
 path("",home,name="home"),
 #path("addtocart/",cart,name="cart"),
 #path("addtocart/,<int:pk>",addtocart,name="addtocart")
 
]
