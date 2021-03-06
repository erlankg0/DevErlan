from django.contrib import admin
from .models import News, Category
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = (
        'id',
        'title',
        'created_at',
        'updated_at',
        'is_published',

    )
    list_display_links = (
        'id',
        'title',
        'created_at',
        'updated_at',

    )
    search_fields = (
        'title',
        'created_at',
        'updated_at',
        'is_published',
        'content',
    )
    list_editable = (
        'is_published',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_display_links = (
        'id',
        'name',
    )
    search_fields = (
        'id',
        'name',
    )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
