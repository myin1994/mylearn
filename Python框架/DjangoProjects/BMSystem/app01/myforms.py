from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01 import models
import re

from django.forms.fields import Field
def title_validate(value):
    title_re = re.compile(r'.*--.*')
    if title_re.match(value):
        raise ValidationError('不能包含--特殊字符')



class BookForm(forms.Form):
    setattr(Field, "error_messages", {
        "required": "不能为空123",
    })
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        lst = [setattr(field, "error_messages", {
            "required": "不能为空123",
        }) for field in self.fields.values()]
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control a b"
            # field.error_messages = {
            #     "required": "不能为空",
            # }

    title = forms.CharField(
        label="书籍名称",
        label_suffix="",
        min_length=1,
        validators=[title_validate, ],
        # widget=forms.TextInput(attrs={"class":"form-control"})
        # error_messages={
        #     "required": "不能为空"
        # }
    )
    price = forms.DecimalField(
        label="价格",
        max_digits=5,
        decimal_places=2
    )
    publish_date = forms.CharField(
        label="出版日期",
        widget=forms.TextInput(attrs={"type": "date"})
    )
    publishs = forms.ModelChoiceField(
        label="出版社",
        queryset=models.Publish.objects.all()
    )
    authors = forms.ModelMultipleChoiceField(
        label="作者",
        # choices=[(1,"name1"),(2,"name2"),(3,"name3")]
        queryset=models.Author.objects.all()
    )
