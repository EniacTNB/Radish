# -*- coding:utf-8 -*8
import xadmin
from .models import EmailVertifyRecord
from .models import Banner
from xadmin import views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "Radish.com"
    site_footer = "萝卜网"
    menu_style = "accordion"


class EmailVertifyRecordAdmin(object):
    list_display = ['code','email','sendTime','send_type',]
    search_fields = ['code','email','send_type',]
    list_filter = ['sendTime','email']

xadmin.site.register(EmailVertifyRecord,EmailVertifyRecordAdmin)

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time' ]
    search_fields = ['title', 'image', 'url','index' ]
    list_filter = ['add_time']
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)