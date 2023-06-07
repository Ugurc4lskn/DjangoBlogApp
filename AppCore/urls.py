from django.urls import path
from .views import (
    index,
    details,
    login_wiew,
    SignUp,
    logout_user,
    categoryFilter
)
urlpatterns = [
    path(route='', view=index, name="index"),
    path(route='blog/post/<int:id>/<slug:post_content>',
         view=details, name="details"),
    path(route='blog/user/login', view=login_wiew, name="login"),
    path(route='blog/user/sign-up', view=SignUp, name="signup"),
    path(route='blog/user/logout', view=logout_user, name='logout'),
    path(route='blog/category/<slug:category>',
         view=categoryFilter, name="category")
]
