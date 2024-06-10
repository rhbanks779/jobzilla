from django.contrib import admin
from .models import Job, Application


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'description', 'location', 'application_deadline')
    search_fields = ('title', 'company_name', 'description', 'location', 'application_deadline')
    list_filter = ('location', 'application_deadline')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'start_date')
    search_fields = ('first_name', 'last_name', 'email', 'start_date')
    list_filter = ('first_name', 'last_name')
    ordering = ('last_name',)
    # readonly_fields = ('start_date',)


# Register your models here.
admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
