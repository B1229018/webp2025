from django.urls import path 
from.import views

#urlpatterns =[
   # path('',views.HelloApiView.as_view(), name='index'),
#]
urlpatterns =[
    path('addcourse', views.add_course, name='add_course'),
    path('courselist', views.list_course, name='list_course'),
]