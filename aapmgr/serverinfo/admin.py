from django.contrib import admin

# Register your models here.
from .models import Asset, Server, patchpeers, appid, aap_patchday

admin.site.register(Asset)
admin.site.register(Server)
admin.site.register(patchpeers)
admin.site.register(appid)
admin.site.register(aap_patchday)



