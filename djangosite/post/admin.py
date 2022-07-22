from django.contrib import admin
from .models import Articles, Comment

# Register your models here.
class Articlesadmin(admin.ModelAdmin):
    list_display = ('id','user','title')

class Commentadmin(admin.ModelAdmin):
    list_display = ('id','article','comment_user')

admin.site.register(Articles,Articlesadmin)
admin.site.register(Comment,Commentadmin)