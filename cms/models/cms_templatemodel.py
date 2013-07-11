from django.db import models
from django.utils.translation import ugettext_lazy as _

from filebrowser.fields import FileBrowseField

class CMS_Template(models.Model):
    
    class Meta:
        app_label = 'cms'
        verbose_name = _('CMS Template')
        verbose_name_plural = _('CMS Template')
   
    cms_template = FileBrowseField(_('CMS Template'), max_length = 500,
                                   extensions = [".html",], directory = 'templates', null = True)
    def __unicode__(self):
        print self.cms_template
        return unicode(self.cms_template)

