from django.db import models
from django.utils.translation import ugettext_lazy as _
# This is a fake model
# cheat with admin site
class PageWizard(models.Model):
    class Meta:
        app_label = 'cms'
        verbose_name = _('Page Wizard')
        verbose_name_plural = _('Page Wizard')
        #model_name = _('Page Wizard')

class ZipUpload(models.Model):
    class Meta:
        app_label = 'cms'
        verbose_name = _('Upload Pictures')
        verbose_name_plural = _('Upload Pictures')
        
    
