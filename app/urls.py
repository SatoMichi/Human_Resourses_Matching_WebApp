from django.urls import path
from . import views

urlpatterns = [
    path("register",views.sign_up,name="register"),                         
    path("set_profile",views.set_info,name="set_profile"),                  
    path("set_image",views.set_image,name="set_image"),                     
    path("",views.index,name="index"),
    path("index",views.index,name="index"),
    path("index/<int:page>",views.index,name="index"),
    path("friends",views.friends,name="friends"),
    path("friends/<int:page>",views.friends,name="friends"),
    path("find",views.find,name="find"),                                    
    path("profile/<int:num>",views.profile,name="profile"),                 
    path("friends_request",views.friends_request,name="friends_request"),   
    path("edit",views.edit,name="edit"),                                    
    path("add/<int:num>",views.add,name="add"),                             
    path("delete/<int:num>",views.delete,name="delete"),
]