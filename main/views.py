from django.shortcuts import render
import instaloader
import requests
from django.http import HttpResponse
from .models import Post

# Create your views here.


def index(request):
    post = Post.objects.all().last()
    image = f"{post.code}.jpg"
    return render(request, "main/index.html", {"post": post, "image": image})


def get_post(request):
    loader = instaloader.Instaloader()
    shortcode = "CyPO7EULn64"
    post = instaloader.Post.from_shortcode(loader.context, shortcode=shortcode)
    post_image = requests.get(post.url).content
    image_route = f"static/{shortcode}.jpg"
    with open(image_route, "wb") as handler:
        handler.write(post_image)
    Post.objects.create(code=shortcode, content=post.caption, image=image_route)
    return HttpResponse("Post saved")
