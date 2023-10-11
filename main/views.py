from django.shortcuts import render
import instaloader
from instaloader import Profile
import requests
from django.http import HttpResponse
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, "main/index.html", {"posts": posts})


def get_post(request):
    loader = instaloader.Instaloader()
    profile = Profile.from_username(loader.context, "popular.front")
    posts = profile.get_posts()
    for post in posts:
        if not Post.objects.filter(code=post.shortcode).exists():
            image = f"{post.shortcode}.jpg"
            with open(f"static/{image}", "wb") as f:
                f.write(requests.get(post.url).content)
            Post.objects.create(code=post.shortcode, content=post.caption, image=image)
    return HttpResponse("Posts saved")
