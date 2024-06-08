from django.contrib import admin

from instagram_app.models import Publication, Comment


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    search_fields = ('id', 'user',)
    exclude = []
    readonly_fields = ('user', 'created_at', 'updated_at',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'publication',)
    search_fields = ('id',)
    exclude = []
    readonly_fields = ('publication', 'user',)


admin.site.register(Publication, PublicationAdmin)
admin.site.register(Comment, CommentAdmin)
