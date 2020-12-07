from django.contrib import admin
from .models import Post, Vote

# Register your models here.
#register classes with admin

admin.site.register(Post)
admin.site.register(Vote)
