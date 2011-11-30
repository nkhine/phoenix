# -*- coding: UTF-8 -*-
# Copyright (C) 2007 Norman Khine <norman@khine.net>

# Import from itools
from itools.core import freeze, merge_dicts
from itools.datatypes import Tokens, Unicode
from itools.gettext import MSG

# Import form ikaaro
from ikaaro.folder import Folder
from ikaaro.registry import register_resource_class, register_document_type
from ikaaro.root import Root
from ikaaro.skins import UI, ui_path

# Import from tzm
from tzm.website import SiteRoot
from tzm.control_panel import CPEditBusinessSector, CPEditBusinessType
#
# Import from here
from views import Chapter_NewInstance, View

class Chapter(SiteRoot):
    
    class_id = 'chapter'
    class_title = MSG(u'Chapter virtual site')
    class_description = MSG(u'Adds a core chapter website.')
    class_icon16 = 'icons/16x16/website.png'
    class_icon48 = 'icons/48x48/website.png'
    class_views = Folder.class_views + ['control_panel']
    class_skin = 'ui/company'
    class_control_panel = ['browse_users', 'add_user', 'edit_virtual_hosts',
                            'edit_security_policy', 'edit_languages',
                            'edit_contact_options', 'broken_links', 'orphans',
                            'edit_industry', 'edit_business', 'edit_business_type']
                            
    class_roles = freeze(['chapter_admin', 'chapter_member'])
    class_schema = merge_dicts(
        SiteRoot.class_schema,
            {'chapter_admin': Tokens(source='metadata',
                                    title=MSG(u"Chapter Administrator"))},
            {'chapter_member': Tokens(source='metadata',
                                    title=MSG(u"Chapter Member"))},
            {'country': Unicode(source='metadata',indexed=True, stored=True)},
            {'region': Unicode(source='metadata',indexed=True, stored=True)},
            {'county': Unicode(source='metadata',indexed=True, stored=True)},
        )

    def _get_resource(self, name):
        if name == 'ui':
            ui = UI(ui_path)
            ui.database = self.metadata.database
            return ui
        # we need to get to the root
        root = self.get_root()
        if name in ('users', 'users.metadata'):
            return root._get_resource(name)
        return SiteRoot._get_resource(self, name)

    def get_document_types(self):
        return []

    ########################################################################
    ## UI
    ########################################################################
    view = View()
    # Industry view
    edit_business = CPEditBusinessSector()
    edit_business_type = CPEditBusinessType()
    new_instance = Chapter_NewInstance() 

class Chapters(Folder):
    class_id = 'chapters'
    class_version = '20111120'
    class_title = MSG(u'Chapters folder')
    class_description = MSG(u'Chapters container.')
    class_icon16 = 'icons/16x16/folder.png'
    class_icon48 = 'icons/48x48/folder.png'
    class_views = ['view', 'browse_content', 'preview_content', 'edit',
                   'last_changes']

    def get_document_types(self):
        return [Chapter]

# Register
register_document_type(Chapter, Root.class_id)