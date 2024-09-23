from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Asset, Server, patchpeers, appid, aap_patchday

class appidResource(resources.ModelResource):
    class Meta:
        model = appid  # or 'core.Book'

class aap_patchdayResource(resources.ModelResource):
    class Meta:
        model = aap_patchday  # or 'core.Book'
class patchpeersResource(resources.ModelResource):
    class Meta:
        model = patchpeers  # or 'core.Book'

class AssetResource(resources.ModelResource):
    class Meta:
        model = Asset   # or 'core.Book'

class ServerResource(resources.ModelResource):
    class Meta:
        model = Server  # or 'core.Book'


class aapidAdmin(ImportExportModelAdmin):
    resource_classes = [appidResource]

class aap_patchdayAdmin(ImportExportModelAdmin):
    resource_classes = [aap_patchdayResource]

class patchpeersAdmin(ImportExportModelAdmin):
    resource_classes = [patchpeersResource]

class AssetAdmin(ImportExportModelAdmin):
    resource_classes = [AssetResource]

class ServerAdmin(ImportExportModelAdmin):
    resource_classes = [ServerResource]


admin.site.register(Asset, AssetAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(patchpeers, patchpeersAdmin)
admin.site.register(aap_patchday, aap_patchdayAdmin)
admin.site.register(appid, aapidAdmin)

