from django.contrib import admin

from instagram_app.models import Profile, Publication, Comment


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    search_fields = ('id', 'user',)
    exclude = []
    readonly_fields = ('user',)


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile',)
    search_fields = ('id', 'profile',)
    exclude = []
    readonly_fields = ('profile', 'created_at', 'updated_at',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'publication',)
    search_fields = ('id',)
    exclude = []
    readonly_fields = ('publication', 'user',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Comment, CommentAdmin)
