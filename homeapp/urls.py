from django.urls import path
from . import views

urlpatterns = [

 path("",views.home,name="home"),
 path("about/",views.about_page,name="aboutus"),
 path("contact/",views.contact,name="contactus"),
 path("home/",views.another_home,name="homepage"),
 path("product/",views.product,name="product"),
 path("new/",views.new,name="new"),

]