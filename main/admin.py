from django.contrib import admin
from .models import VisitorLog

@admin.register(VisitorLog)
class VisitorLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'ip_address', 'path', 'method', 'user_agent')
    search_fields = ('ip_address', 'path', 'user_agent')
    readonly_fields = [f.name for f in VisitorLog._meta.fields]

    def has_add_permission(self, request):
        return False
