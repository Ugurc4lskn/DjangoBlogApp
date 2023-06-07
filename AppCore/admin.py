from django.contrib import admin
from .models import (
    BlogPost,
    TagModel,
    UserProfileModel,
    CategoryModel,
    Reklam,
    Comment
)


@admin.register(Reklam)
class ModelReklam(admin.ModelAdmin):
    list_display = ('image_rightUp', 'image_righend', 'image_article')


@admin.register(BlogPost)
class ModelPost(admin.ModelAdmin):
    list_display = ('title', 'published', 'published_date', "user")
    search_fields = ('title',)
    list_per_page = 20


@admin.register(CategoryModel)
class ModelCategory(admin.ModelAdmin):
    list_display = ('category', )
    search_fields = ('category', )
    list_per_page = 20


@admin.register(TagModel)
class ModelTags(admin.ModelAdmin):
    list_display = ('tag', )
    search_fields = ('tag',)
    list_per_page = 20


@admin.register(UserProfileModel)
class ModelUserProfile(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user',)
    list_per_page = 20


@admin.register(Comment)
class ModelComment(admin.ModelAdmin):
    list_display = ('id', 'post_title', 'user', 'created_date', 'content')

    def post_title(self, obj):
        return obj.post.title

    post_title.short_description = "Post Title"
    post_title.admin_order_field = 'post__title'
