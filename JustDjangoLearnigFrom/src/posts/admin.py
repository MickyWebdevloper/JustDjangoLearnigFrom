from django.contrib import admin

from . models import Post, Category, Author, Tages

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','author']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','user']

@admin.register(Tages)
class TagesAdmin(admin.ModelAdmin):
    list_display = ['id','title']