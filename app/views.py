from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from app.models import Post

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()

    return render(request, "app/index.html", {"post_list": qs})


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(
        request,
        "app/post_detail.html",
        {
            "post": post,
        },
    )
