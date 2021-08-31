from django.contrib import admin
from django.db import models
from .models import Hospice_Service, Care_Service, Respite_Service, Therapy_Service, Companion_Service, IV_Therapy_Service, Nursing_Service, Social_Service, Aid_Service, Homemaking_Service, Interpretive_Service, Assistant_Service, Living_Skills_Service
# Register your models here.
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group

admin.site.site_header = "Melodiahomecare Admin"
admin.site.site_title = "Melodiahomecare Admin Portal"
admin.site.index_title = "Welcome to Melodiahomecare Admin Portal"

admin.site.unregister(Group)


class Disable_Admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(Living_Skills_Service,
                    Disable_Admin)
admin.site.register(Hospice_Service, Disable_Admin)
admin.site.register(Respite_Service, Disable_Admin)
admin.site.register(Therapy_Service, Disable_Admin)
admin.site.register(Companion_Service, Disable_Admin)
admin.site.register(IV_Therapy_Service, Disable_Admin)
admin.site.register(Nursing_Service, Disable_Admin)
admin.site.register(Social_Service, Disable_Admin)
admin.site.register(Aid_Service, Disable_Admin)
admin.site.register(Assistant_Service, Disable_Admin)
admin.site.register(Interpretive_Service, Disable_Admin)
admin.site.register(Homemaking_Service, Disable_Admin)
admin.site.register(Care_Service, Disable_Admin)
