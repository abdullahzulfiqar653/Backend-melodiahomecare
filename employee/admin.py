from django.contrib import admin
from .models import *
# Register your models here.


class Disable_Admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(Employee_Benefits, Disable_Admin)
