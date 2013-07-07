import os
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cms.plugins.picture.models import Picture
from cms.utils.conf import get_cms_setting

class PicturePlugin(CMSPluginBase):
    model = Picture
    name = _("Picture")
    render_template = "cms/plugins/picture.html"
    text_enabled = True
    svg_template = "cms/plugins/picture_svg.html"

    def render(self, context, instance, placeholder):
        # @wej modify here, check context, to see what mode now
        # if the mode is draft, then we should generate our url
        # add a new js file in chang_form.html so support the external digalog
        if instance.url:
            link = instance.url
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""

        alt = instance.alt
        longdesc = instance.longdesc
        onclick_action = None
        # @wej modified here if context = design
        # we will put desgin in views.py
        if context.has_key('design'):
            alt = "This is for " + placeholder
            # fetch edit url
            cms_admin_site = context['request'].session.get('cms_admin_site', None)
            edit_url = reverse('admin:cms_page_edit_plugin',
                               args=(instance.pk,),
                               current_app=cms_admin_site)
            # @wej we need use more generalize method to deal with the situation
            js_template = Template( "javascript:window.open('{{target_url}}', '{{placeholder}}', 'width=800,height=600,menubar=yes')")
            onclick_action = js_template.render(Context({ 'target_url': edit_url, 'placeholder':placeholder }))
            link = 'javascript:void(0)'
            longdesc = alt
            
        # if image is none
        if context.has_key('default') or (not instance.image):
            page_id = instance.placeholder.page.pk
            image_path = settings.DEFAULT_IMAGE_PATH \
                + '/' + str(page_id) \
                + '/' + str(instance.pk) + '.png'
            if os.path.exists(settings.MEDIA_ROOT + '/' + image_path):
                instance.image = settings.MEDIA_URL + '/' + image_path
            else:
                # ToDo: @wej pengding Thu Jun 20 20:19:20 CST 2013
                instance.image = get_cms_setting('PAGE_MEDIA_PATH') + 'default/' + 'all.png'
        
        context.update({
            'picture': instance,
            'link': link,
            'placeholder': placeholder,
            'alt': alt,
            'longdesc': longdesc,
            'onclick_action': onclick_action
        })
        return context

    def icon_src(self, instance):
        # TODO - possibly use 'instance' and provide a thumbnail image
        return settings.STATIC_URL + u"cms/images/plugins/image.png"

plugin_pool.register_plugin(PicturePlugin)
