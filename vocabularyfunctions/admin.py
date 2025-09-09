from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.html import format_html
from .models import VocabItem

# Register your models here
@admin.register(VocabItem)
class VocabItemAdmin(admin.ModelAdmin):
    list_display = ('word', 'english_meaning', 'gender', 'part_of_speech', 'user')
    search_fields = ('word', 'english_meaning', 'user__username')

class UserVocabInline(admin.TabularInline):
    model = VocabItem
    extra = 0
    fields = ('word', 'english_meaning', 'gender', 'part_of_speech', 'other_comments')
    readonly_fields = fields

try:
    admin.site.unregister(get_user_model())
except admin.sites.AlreadyRegistered:
    pass

@admin.register(get_user_model())
class CustomUserAdmin(DefaultUserAdmin):
    list_display = ('username', 'email', 'vocab_count') + DefaultUserAdmin.list_display[3:]
    inlines = [UserVocabInline]
    search_fields = ('username', 'email')

    def vocab_count(self, obj):
        return obj.vocab_items.count()
    vocab_count.short_description = 'Vocab Count'
