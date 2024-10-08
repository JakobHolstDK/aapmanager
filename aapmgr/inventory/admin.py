from django.contrib import admin

# Register your models here.
from .models import server, zone, region, appid, environment, serverrole, project

admin.site.register(server)
admin.site.register(zone)
admin.site.register(region)
admin.site.register(appid)
admin.site.register(environment)
admin.site.register(serverrole)
admin.site.register(project)


