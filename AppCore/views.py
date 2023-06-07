from django.shortcuts import redirect, HttpResponse, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils.html import escape
from .models import (
    BlogPost,
    Reklam,
    Comment,
    CategoryModel

)

from .forms import UserForm, UserLoginForm, CommentForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def index(request):
    post = BlogPost.objects.filter(published=True)
    categorys = CategoryModel.objects.filter(view=True)
    images = Reklam.objects.all()

    paginator = Paginator(post, 10)
    page_number = request.GET.get("page")
    allpost = paginator.get_page(page_number)

    return render(
        request=request,
        template_name="index.html",
        context={
            "post": allpost,
            "image": images,
            "status": True,
            "category": categorys
        }
    )


def details(request, id, post_content):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():

            coment = escape(form.cleaned_data.get("comment"))
            print(coment)
            Comment.objects.create(
                user=request.user,
                post_id=id,
                content=coment
            )
            messages.success(
                request,
                "Mesaj eklendi",
            )
            return redirect(request.path)
        else:
            messages.error(
                request,
                "Mesaj eklenmedi! Tekrar deneyin",
            )
            return redirect(request.path)

    else:
        form = CommentForm(request.POST)
        comment = Comment.objects.filter(post_id=id)
        categorys = CategoryModel.objects.filter(view=True)
        detail = BlogPost.objects.get(pk=id)
        context = {
            "post": detail,
            "status": True,
            "form": form,
            "comments": comment,
            "category": categorys,
        }
        return render(request=request, template_name="detail.html", context=context)


def SignUp(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = escape(form.cleaned_data.get("username"))
            password = escape(form.cleaned_data.get("password"))
            repassword = escape(form.cleaned_data.get("repassword"))

            if (password != repassword and not User.objects.filter(username=username).first()):
                messages.error(
                    request,
                    "Bir hata oluştu ! Tekrar deneyin",
                )
                return redirect(request.path)

            else:
                User.objects.create_user(
                    username=username, email=None, password=password
                ).save()
                messages.success(
                    request,
                    "Hesap oluştu lütfen giriş yapınız.",
                )
                return redirect(request.path)
        else:

            messages.error(
                request,
                "Bir hata oluştu tekrar deneyin",
            )
            return redirect(request.path)

    else:
        form = UserForm(request.POST)
        categorys = CategoryModel.objects.filter(view=True)
        return render(request=request, template_name="signup.html", context={"form": form, "category": categorys, })


def login_wiew(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            __username = escape(form.cleaned_data.get("username"))
            __password = escape(form.cleaned_data.get("password"))

            user = authenticate(
                request, username=__username, password=__password)
            if user is not None:
                login(request, user)
                return redirect("index")
        else:
            messages.error(
                request,
                "Bir hata oluştu tekrar deneyin",
            )
            return redirect("login")

    else:
        form = UserLoginForm(request.POST)
        categorys = CategoryModel.objects.filter(view=True)
        context = {
            "form": form,
            "category": categorys,
        }
        return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    return redirect("login")


def categoryFilter(request, category: str):
    categorys = CategoryModel.objects.filter(view=True)
    categoryModel = CategoryModel.objects.get(slug=category)
    content = BlogPost.objects.filter(category=categoryModel.id)

    images = Reklam.objects.all()

    paginator = Paginator(content, 10)
    page_number = request.GET.get("page")
    allpost = paginator.get_page(page_number)

    context = {
        "category": categorys,
        "content": allpost,
        "image": images,
        "status": True

    }
    return render(request, "category.html", context)
