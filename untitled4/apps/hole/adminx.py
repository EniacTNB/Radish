# -*- coding: utf-8 -*-
__programmer__ = 'Eniac'
__date__ = '2018/7/13 下午4:17'

from .models import Hole
from .models import Hole_people
import xadmin

class HoleAdmin(object):
    list_display = ['company','desc','prov','disc','concrate_address','addtime']
    search_fields = ['company','prov','disc']
    list_filter = ['prov','disc','addtime']

xadmin.site.register(Hole,HoleAdmin)

class Hole_peopleAdmin(object):

    list_display = ['name','company','work_year','gender','occupation','addtime']
    search_fields = ['name','company','gender','work_year','occupation']
    list_filter = ['gender','addtime']

xadmin.site.register(Hole_people,Hole_peopleAdmin)