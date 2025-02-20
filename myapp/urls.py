from django.urls import path
from . import views

urlpatterns =[
    path("hello/",views.hello),
    path("info/",views.info),
    path("input/",views.input),
    path("watch/",views.watch),
    path("site/", views.home)
]