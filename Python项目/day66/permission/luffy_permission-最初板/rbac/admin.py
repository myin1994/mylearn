from django.contrib import admin

# Register your models here.
from rbac import models


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id','url','access_name','menu','icon','parent']
    list_editable = ['url','access_name','menu','icon','parent']


admin.site.register(models.UserInfo)
admin.site.register(models.TopMenu)
admin.site.register(models.Role)
admin.site.register(models.Permission,PermissionAdmin)