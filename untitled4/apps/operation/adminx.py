# -*- coding: utf-8 -*-
__programmer__ = 'Eniac'
__date__ = '2018/7/13 下午10:52'

from .models import UserMessage
from .models import Hole_People_Favt
from .models import Comment
import xadmin

class UserMessageAdmin(object):
    list_display = ['user','message','has_read','add_time']
    search_fields = ['user','message','has_read']
    list_filter = ['add_time','user','message']

xadmin.site.register(UserMessage,UserMessageAdmin)

class CommentAdmin(object):

    list_display = ['name','mobile','comment','add_time']
    search_fields = ['name','mobile']
    list_filter = ['add_time']
xadmin.site.register(Comment,CommentAdmin)

class Hole_People_FavtAdmin(object):
    list_display = ['user','radish','resume','add_time']
    list_filter = ['add_time','user']
    search_fields = ['user','radish','resume']
xadmin.site.register(Hole_People_Favt,Hole_People_FavtAdmin)