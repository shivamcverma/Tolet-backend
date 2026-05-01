from django.contrib import admin
from .models import Favorite, Report

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'created_at')
    search_fields = ('user__username', 'property__title')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'created_at', 'is_resolved')
    list_filter = ('is_resolved', 'created_at')
    search_fields = ('user__username', 'property__title', 'reason')
    
    actions = ['mark_resolved']

    def mark_resolved(self, request, queryset):
        queryset.update(is_resolved=True)
    mark_resolved.short_description = "Mark selected reports as resolved"

admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Report, ReportAdmin)
