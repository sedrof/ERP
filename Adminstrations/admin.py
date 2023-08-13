from django.apps import apps
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.admin.models import LogEntry

# Get all installed apps
installed_apps = apps.get_app_configs()

class LogEntryAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_max_show_all = 50
    readonly_fields = ("content_type", "user", "action_time")
    list_display = ["content_type", "user", "object_repr", "action_time", "action_flag"]
    search_fields = ["user__username", "object_repr"]
    actions = ["fast_delete"]

    def fast_delete(self, request, queryset):
        LogEntry.objects.all().delete()

    fast_delete.short_description = "FAST DELETE"

admin.site.register(LogEntry, LogEntryAdmin)
# Loop through each app and its models
for app in installed_apps:
    models = app.get_models()
    for model in models:
        if model not in [Group, User, LogEntry]:
            admin.site.register(model)