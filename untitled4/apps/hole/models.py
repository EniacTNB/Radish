# _*_ encoding:utf-8 _*_

from django.db import models
from datetime import datetime

# Create your models here.



class Hole(models.Model):

    company = models.CharField(max_length=30,verbose_name=u"坑主公司")
    desc = models.TextField(verbose_name=u"坑主描述")
    prov = models.CharField(max_length=20, verbose_name=u"省份")
    disc = models.CharField(max_length=20, verbose_name=u"区/乡镇")
    concrate_address = models.TextField(verbose_name=u"详细地址")
    addtime = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"坑"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.company

class Hole_people(models.Model):
    name = models.CharField(max_length=30,verbose_name=u"坑主名称")
    company= models.ForeignKey(Hole,verbose_name=u"所属公司")
    work_year = models.IntegerField(default=0,verbose_name=u"工作年龄")
    gender = models.CharField(choices=(("male",u"男"),("female",u"女")),max_length=6,verbose_name=u"性别")
    occupation = models.CharField(max_length=30,verbose_name=u"职位")
    addtime = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"坑主"
        verbose_name_plural =verbose_name
