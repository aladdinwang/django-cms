from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from cms.models.fakemodel import UploadZip

class UploadZipAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        print requset.user
        
    def has_add_permission(self, request):
        return False

# admin.site.register(UploadZip, UploadZipAdmin)
