from django.contrib import admin
from .models import *
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False
    readonly_fields = ['first_name', 'last_name', 'address',
                       'city', 'state', 'zip_code', 'email', 'phone', 'questions']


admin.site.register(Contact, ContactAdmin)
