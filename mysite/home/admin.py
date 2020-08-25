from django.contrib import admin

# Register your models here.
from home.models import Contact, Comment


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'create_at', 'status')
    list_filter = ('status', 'create_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'create_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'subject', 'message', 'rating', 'status', 'create_at')
    list_filter = ('status', 'create_at')
    readonly_fields = ('product', 'user', 'subject', 'message', 'rating')
    list_display_links = ('subject', 'product')
    list_editable = ('status',) #list üzerinden düzenleme



admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
