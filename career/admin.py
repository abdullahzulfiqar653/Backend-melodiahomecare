from django.contrib import admin
from .models import *
# Register your models here.


class Disable_Admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


class BranchAdmin(admin.ModelAdmin):
    fields = ('branch_name', 'branch_address',
              'email', 'phone', 'fax', 'team_image')


class Apply_FormsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False
    readonly_fields = ['application_date', 'position', 'location', 'about', 'reffer', 'under_18', 'other_company_work', 'employeed',
                       'first_name', 'last_name', 'address1', 'address2', 'city', 'state', 'zip_code', 'email', 'phone', 'available', 'travel', 'cv', 'signature']


admin.site.register(Employee_Benefits, Disable_Admin)

admin.site.register(Job_Opening)
admin.site.register(Areas, Disable_Admin)
admin.site.register(Team)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Apply_Now)
