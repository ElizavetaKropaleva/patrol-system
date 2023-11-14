from django.contrib import admin

from patrol.models import OsData, CpuData, Logs


class OsDataAdmin(admin.ModelAdmin):
    fieldsets = [
        ('OS', {'fields': ['OS']}),
        ('description', {'fields': ['description']}),
        ('release', {'fields': ['release']}),
        ('codename', {'fields': ['codename']}),
        ('architecture', {'fields': ['architecture']}),
        ('kernel', {'fields': ['kernel']}),
        ('type', {'fields': ['type']})
    ]


class CpuDataAdmin(admin.ModelAdmin):
    fieldsets = [
        ('modes', {'fields': ['modes']}),
        ('vendor', {'fields': ['vendor']}),
        ('model', {'fields': ['model']}),
        ('CPUs', {'fields': ['CPUs']}),
        ('threads', {'fields': ['threads']}),
        ('cores_per_socket', {'fields': ['cores_per_socket']}),
        ('sockets', {'fields': ['sockets']})
    ]


class LogsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('date', {'fields': ['date']}),
        ('time', {'fields': ['time']}),
        ('function', {'fields': ['function']}),
        ('event', {'fields': ['event']})
    ]


admin.site.register(OsData, OsDataAdmin)
admin.site.register(CpuData, CpuDataAdmin)
admin.site.register(Logs, LogsAdmin)
