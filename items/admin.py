from django.contrib import admin

from items.models import Item, Like, Comment


class LikeInline(admin.TabularInline):
    model = Like


class ArtAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name')
    list_filter = ('type', 'id')
    inlines = (
        LikeInline,
    )


admin.site.register(Item, ArtAdmin)
admin.site.register(Comment)
admin.site.register(Like)
