from django.urls import path
import main.views as main

urlpatterns = [
    path("", main.index, name="index"),
    path("get_post", main.get_post, name="get_post"),
]
