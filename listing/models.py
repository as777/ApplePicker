from django.db import models
from django.contrib.auth.models import User

# field reference

# Create your models here.

class Item(models.Model):

    name = models.CharField(max_length=255)

    description = models.TextField(help_text="why me")

    is_done = models.BooleanField(default=False)

    date_entry = models.DateTimeField(auto_now_add=True)

    TVSHOW = 'S'
    MOVIE = 'M'
    DOCUMENTARY = 'D'
    CATEGORY_CHOICES = (
        (TVSHOW, 'TV Show'),
        (MOVIE, 'Movie'),
        (DOCUMENTARY, 'Documentary'),
        (None, 'No Category')
    )
    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
        default= None,
    )

    def __str__(self):
        return self.name


# class Category(models.Model):
#     class Meta:
#         verbose_name_plural = "Categories"
#
#     title = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.title
