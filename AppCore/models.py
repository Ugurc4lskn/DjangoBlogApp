from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Reklam(models.Model):
    image_rightUp = models.ImageField(
        verbose_name='reklamalani',
        upload_to='images/reklamright/%Y/%m/%d',
        default='images/300x600.jpg',
        blank=True
    )
    image_righend = models.ImageField(
        verbose_name='reklamalani',
        upload_to='images/reklamright/%Y/%m/%d',
        default='images/300x250.jpg',
        blank=True
    )
    image_article = models.ImageField(
        verbose_name='reklamalani',
        upload_to='images/reklamarticle/%Y/%m/%d',
        default='images/728x90.png',
        blank=True
    )


class CategoryModel(models.Model):
    category = models.CharField(
        verbose_name="category_name",
        max_length=200,
        default=""
    )
    slug = models.SlugField(default="")
    view = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category.replace('ı', "i"))
        super(CategoryModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.category


class TagModel(models.Model):
    tag = models.CharField(
        verbose_name='tags_name',
        max_length=200,
        default=''
    )

    def __str__(self) -> str:
        return self.tag


class UserProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.CharField(
        verbose_name="hakkinda",
        default='',
        max_length=300,
        null=True,
        blank=True
    )
    webSite = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    profile_image = models.ImageField(
        verbose_name='profil_resmi',
        upload_to='images/user/%Y/%m/%d',
        blank=True

    )

    def __str__(self):
        return self.user.username


class BlogPost(models.Model):
    title = models.CharField(
        default='',
        max_length=300,
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        UserProfileModel, on_delete=models.CASCADE, default='')

    desription = models.CharField(
        default='',
        max_length=400,

    )
    content = models.TextField()
    tag = models.ManyToManyField(
        to=TagModel,
        blank=True

    )
    category = models.ManyToManyField(
        to=CategoryModel,
        blank=True

    )
    published = models.BooleanField(
        default=False
    )
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        verbose_name='main_image',
        upload_to='images/post/%Y/%m/%d',
        blank=True

    )

    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ['-published_date']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace('ı', 'i'))
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
