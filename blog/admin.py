from django.contrib import admin
from blog.models import Tag, Post
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)




# Register your models here.
