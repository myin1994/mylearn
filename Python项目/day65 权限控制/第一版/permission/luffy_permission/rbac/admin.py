from django.contrib import admin
from rbac import models


class PermissionAdmin(admin.ModelAdmin):
	list_display = ['id','title','url' ]
	list_editable = ['title','url']


admin.site.register(models.Permission, PermissionAdmin)
admin.site.register(models.Role)
admin.site.register(models.User)
