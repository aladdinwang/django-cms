from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from cms.models.fakemodel import PageWizard

class PageWizardAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return HttpResponseRedirect("/admin/masterpage/")
    def has_add_permission(self, request):
        return False

admin.site.register(PageWizard, PageWizardAdmin)
    
