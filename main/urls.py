from django.urls import path
from . import views
urlpatterns =[
    path("home/",views.home, name="index"),
    path('<int:id>',views.index,name="index"),
    path("<str:name>",views.index2,name="name"),
    path("create/",views.create,name="create")
    
]
