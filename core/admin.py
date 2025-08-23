from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import Worker, Studio, Game


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('position', 'studio')
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {'fields': ('position', 'studio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {'fields': ('first_name', 'last_name', 'position', 'studio')}),
    )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('genre', 'studio')

admin.site.register(Studio)