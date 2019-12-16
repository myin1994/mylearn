from django.contrib import admin

# Register your models here.
from rbac import models


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id','url','access_name','is_menu','icon']
    list_editable = ['url','access_name','is_menu','icon']


admin.site.register(models.UserInfo)
admin.site.register(models.Role)
admin.site.register(models.Permission,PermissionAdmin)