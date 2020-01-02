from django.contrib import admin
from tabledata.models import BH_GM_DOCK, Location, DQ_FAILURE, BH_GM_Constraint_Dock


class BH_GM_DOCKAdmin(admin.ModelAdmin):
    readonly_fields = ['bh_gm_dock_id',]


class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ['location_id',]

admin.site.register(DQ_FAILURE)
admin.site.register(BH_GM_DOCK, BH_GM_DOCKAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(BH_GM_Constraint_Dock)
