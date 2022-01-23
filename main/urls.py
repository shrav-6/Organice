from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.urls import include,re_path
urlpatterns =[
    path("",views.home, name="home"),
    path("home/",views.home, name="home"),
    path('list<int:id>/',views.viewlist,name="viewlist"),
    path("createlist/",views.createlist,name="createlist"),
    path("createnote/",views.createnote,name="createnote"),
    path("note<int:id>/", views.viewnote, name="viewnote"),
    path("view_all_lists/",views.view_all_lists,name="view_all_lists"),
    path("view_all_notes/",views.view_all_notes,name="view_all_notes")
    #path('favicon.ico/', RedirectView.as_view(url='/static/img/favicon/favicon.ico')),
    #path('favicon.ico/', RedirectView.as_view(url='/static/image/favicon.ico')),
]
