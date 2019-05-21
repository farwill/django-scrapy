from django.contrib import admin
from .models import Quote, Tag

# Register your models here.
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_tags',)

    def get_tags(self, obj):
        return ",".join([tag.name for tag in obj.tags.all()])

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', "get_quote_count",)

    def get_quote_count(self, obj):
        return obj.quote_set.count()