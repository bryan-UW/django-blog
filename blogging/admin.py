from django.contrib import admin

from blogging.models import Post, Category


class CategoryInlineAdmin(admin.TabularInline):
    model = Category.posts.through  


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInlineAdmin] 

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)  


# admin.site.register(Post)
# admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)