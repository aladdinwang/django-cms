from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from cms.models.cms_templatemodel import CMS_Template

class CMS_TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'cms_template', )
    search_field = ('name', 'cms_template', )

admin.site.register(CMS_Template, CMS_TemplateAdmin)
