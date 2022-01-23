from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.urls import include,re_path
urlpatterns =[
    path("",views.home, name="index"),
    path("home/",views.home, name="index"),
    path('<int:id>',views.index,name="index"),
    path("<str:name>",views.index2,name="name"),
    path("create/",views.create,name="create"),
    #path('favicon.ico/', RedirectView.as_view(url='/static/img/favicon/favicon.ico')),
    #path('favicon.ico/', RedirectView.as_view(url='/static/image/favicon.ico')),
]
