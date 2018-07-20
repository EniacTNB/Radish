# _*_ encoding:utf-8 _*_

from django.db import models
from datetime import datetime
# Create your models here.


class Radish_info(models.Model):
    name = models.CharField(max_length=5,verbose_name="姓名",default='NULL')
    gender = models.CharField(choices=(("male",u"男"),("female",u"女")),max_length=6,verbose_name=u"性别")
    age = models.IntegerField(default=0,verbose_name=u"年龄")
    work_age = models.IntegerField(default=10,verbose_name=u"工作年限")
    education_background = models.CharField(choices=(("chuzhong",u"初中"),("zhongji",u"中技"),("gaozhong",u"高中"),("zhongzhuan",u"中专"),("dazhuan",u"大专"),("benke",u"本科"),("shuoshi",u"硕士"),("mba",u"MBA"),("boshi",u"博士"),("emba",u"EMBA"),("qita",u"其他")),max_length=20,verbose_name= u"学历")
    address_now = models.CharField(max_length=20,verbose_name=u"现居住地")
    company_now = models.CharField(max_length=30,verbose_name=u"当前公司")
    occupation_now = models.CharField(max_length=30,verbose_name=u"当前职位")
    filename = models.CharField(max_length=20,verbose_name=u"简历名称")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"上传时间")
    contact = models.IntegerField(default=12,verbose_name=u"联系方式")
    image = models.ImageField(upload_to="radish/%Y/m",verbose_name=u"头像")

    class Meta:

        verbose_name = u"萝卜信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Resume(models.Model):
    Radish_info = models.ForeignKey(Radish_info,verbose_name=u"萝卜")
    name = models.CharField(max_length=30,verbose_name=u"简历名称")
    file = models.FileField(upload_to="radish/%Y/%m",max_length=100,verbose_name=u"资源查看或者下载")
    add_time = models.DateTimeField(verbose_name="上传时间",default=datetime.now)

    class Meta:
        verbose_name = u"简历"
        verbose_name_plural = verbose_name