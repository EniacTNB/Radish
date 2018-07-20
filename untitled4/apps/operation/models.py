# _*_ encoding:utf-8 _*_

from django.db import models
from datetime import datetime
from users.models import UserProfile
from radish.models import Radish_info
from radish.models import Resume
# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"姓名")
    mobile = models.CharField(max_length=11,verbose_name=u"手机")
    comment = models.TextField(verbose_name=u"评论")
    add_time  = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(UserProfile,verbose_name=u"用户")
    class Meta:
        verbose_name = u"评价"
        verbose_name_plural = verbose_name


class Hole_People_Favt(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u"用户")
    radish = models.ForeignKey(Radish_info,verbose_name=u"萝卜")
    resume = models.ForeignKey(Resume,verbose_name=u"简历")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"收藏简历"
        verbose_name_plural = verbose_name

class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name=u"接受用户")
    message = models.CharField(max_length=400,verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False,verbose_name=u"已读")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name