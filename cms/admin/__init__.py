# -*- coding: utf-8 -*-
import pageadmin
import useradmin
import permissionadmin
import pagewizardadmin
#import cms_templateadmin

# Piggyback off admin.autodiscover() to discover cms plugins
from cms import plugin_pool
from cms.apphook_pool import apphook_pool
plugin_pool.plugin_pool.discover_plugins()

apphook_pool.discover_apps()
