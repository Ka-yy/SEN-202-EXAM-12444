from django.contrib import admin
from .models import Manager, Intern

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'email', 'department', 'has_company_card', 'team_size', 'is_active']
    list_filter = ['department', 'has_company_card', 'is_active', 'hire_date']
    search_fields = ['first_name', 'last_name', 'email', 'department']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Employment Details', {
            'fields': ('hire_date', 'salary', 'is_active')
        }),
        ('Manager Specific', {
            'fields': ('department', 'has_company_card', 'team_size', 'budget_limit')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'email', 'mentor', 'internship_end', 'university', 'is_active']
    list_filter = ['mentor', 'internship_end', 'is_active', 'university']
    search_fields = ['first_name', 'last_name', 'email', 'university', 'field_of_study']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Employment Details', {
            'fields': ('hire_date', 'salary', 'is_active')
        }),
        ('Intern Specific', {
            'fields': ('mentor', 'internship_end', 'university', 'field_of_study')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
