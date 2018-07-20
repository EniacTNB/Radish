# -*- coding: utf-8 -*-
__programmer__ = 'Eniac'
__date__ = '2018/7/13 上午11:47'

from .models import Resume
from .models import Radish_info
import xadmin


class ResumeAdmin(object):
    list_display = ['Radish_info','name','file']
    list_filter = ['Radish_info','add_time']
    search_fields = ['Radish_info']

xadmin.site.register(Resume,ResumeAdmin)

class Radish_infoAdmin(object):

    list_display = ['name','gender','work_age','age','education_background','company_now','occupation_now','add_time']
    search_fields = ['gender','work_age','age','education_background','occupation_now','name']
    list_filter = ['gender','education_background','occupation_now','company_now','add_time']

xadmin.site.register(Radish_info,Radish_infoAdmin)