
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from cms.models import CMSPlugin, Page
from filebrowser.fields import FileBrowseField
from os.path import basename

class Picture(CMSPlugin):
    """
    A Picture with or without a link.
    """
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    FLOAT_CHOICES = ((LEFT, _("left")),
                     (RIGHT, _("right")),
                     (CENTER, _("center")),
                     )
    image = FileBrowseField(_("image"), max_length = 500, extensions = [".jpg", ".png", "jpeg"], directory="default/", blank = True, format = "Image")
    url = models.CharField(_("link"), max_length=255, blank=True, null=True,
        help_text=_("If present, clicking on image will take user to link."))
    page_link = models.ForeignKey(Page, verbose_name=_("page"), null=True,
        blank=True, help_text=_("If present, clicking on image will take user \
        to specified page."))
    alt = models.CharField(_("alternate text"), max_length=255, blank=True,
        null=True, help_text=_("Specifies an alternate text for an image, if \
        the image cannot be displayed.<br />Is also used by search engines to \
        classify the image."))
    longdesc = models.CharField(_("long description"), max_length=255,
        blank=True, null=True, help_text=_("When user hovers above picture,\
        this text will appear in a popup."))

    width = models.CharField(_("picture width"), max_length=255, blank=True, help_text=
                                _("Example: '50px', '80%'.If offered, please also set picture height"))
    height = models.CharField(_("picture height"), max_length=255, blank=True, help_text=
                                _("Example: '50px', '80%'.If offered, please also set picture width"))
    float = models.CharField(_("side"), max_length=10, blank=True, null=True,
        choices=FLOAT_CHOICES, help_text=_("Move image left, right or center."))

    def __unicode__(self):
        if self.alt:
            return self.alt[:40]
        elif self.image:
            # added if, because it raised attribute error when file wasn't
            # defined.
            try:
                return u"%s" % basename(self.image.path)
            except:
                pass
        return "<empty>"

    def clean(self):
        if self.url and self.page_link:
            raise ValidationError(
                             _("You can enter a Link or a Page, but not both."))
