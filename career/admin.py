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


admin.site.register(Employee_Benefits, Disable_Admin)

admin.site.register(Job_Opening)
admin.site.register(Areas, Disable_Admin)
admin.site.register(Team)
admin.site.register(Branch, BranchAdmin)
