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
        print(f"Downloading post: {post.shortcode}")
        if not Post.objects.filter(code=post.shortcode).exists():
            if post.is_video:
                image = f"{post.shortcode}.mp4"
                with open(f"static/{image}", "wb") as f:
                    f.write(requests.get(post.video_url).content)
            else:
                image = f"{post.shortcode}.jpg"
                with open(f"static/{image}", "wb") as f:
                    f.write(requests.get(post.url).content)
            Post.objects.create(code=post.shortcode, content=post.caption, image=image)
    return HttpResponse("Posts saved")
