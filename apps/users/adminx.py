import xadmin
from .models import Banner,UserProfile,EmailVerifyRecord
from xadmin import views

class EmailVerifyRecordAdmin(object):
    pass



class BannerAdmin(object):
    list_display = [ 'title','url','index']



class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'XXXX教育管理系统'
    site_footer = 'XXXX'
    menu_style = 'accordion'



xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
