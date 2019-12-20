from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from rbac import models
from django.utils.safestring import mark_safe

class RoleModelForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = '__all__'
        exclude = ['permissions']

    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

from rbac.tools.icons import icon_list
class TopMenuModelForm(forms.ModelForm):
    class Meta:
        model = models.TopMenu
        fields = ['title','weight','icon']
        # fields = '__all__'


    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name, field in self.fields.items():
            if name == 'icon':
                field.widget = forms.RadioSelect(choices=[[i[0],mark_safe(i[1])] for i in icon_list])
                continue
            field.widget.attrs.update({'class':'form-control'})

class PermissionModelForm(forms.ModelForm):
    class Meta:
        model = models.Permission
        fields = '__all__'

    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

#批量添加权限使用
class AccessModelForm(forms.ModelForm):
    class Meta:
        model = models.Permission
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
            if name == 'parent':
                field.choices =  [(None, '-------')] + list(
            models.Permission.objects.filter(parent__isnull=True).exclude(
                menu__isnull=True).values_list('id', 'access_name'))

    def clean(self):
        menu = self.cleaned_data.get('menu')
        pid = self.cleaned_data.get('parent')

        if menu and pid:
            raise forms.ValidationError('菜单和根权限同时只能选择一个')
        return self.cleaned_data