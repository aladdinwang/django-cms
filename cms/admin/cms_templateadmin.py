from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from cms.models.cms_templatemodel import CMS_Template

class CMS_TemplateAdmin(admin.ModelAdmin):
    list_display = ('cms_template', )
    search_field = ('cms_template', )

admin.site.register(CMS_Template, CMS_TemplateAdmin)
