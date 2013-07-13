from django.db import models
from django.utils.translation import ugettext_lazy as _

from filebrowser.fields import FileBrowseField

class CMS_Template(models.Model):
    
    class Meta:
        app_label = 'cms'
        verbose_name = _('CMS Template')
        verbose_name_plural = _('CMS Template')

    name = models.CharField(_('Name'), max_length=500, blank=True, 
                            help_text=_('The name used to be searched in order to find the template.'),
                            db_index=True)
    cms_template = FileBrowseField(_('CMS Template'), max_length = 500,
                                   extensions = [".html",], directory = 'templates', null = True)
    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        path = str(self.cms_template).split('/media/templates/')[1]
        return path.strip()
