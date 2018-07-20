# _*_ encoding:utf-8 _*_
from django.db import models
from datetime import datetime
# Create your models here.


from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name="nickname",default="User")
    birthday = models.DateField(verbose_name="birthday",null=True,blank=True)
    gender = models.CharField(max_length= 7,choices=(("male",u"男"),("female",u"女")),default="female")
    address = models.CharField(max_length=100,verbose_name="address",default="")
    mobile = models.CharField(max_length=11,verbose_name="mobile",null=True,blank=True)
    occupation = models.CharField(max_length= 40,verbose_name="occuption",default="")
    company = models.CharField(max_length=50,verbose_name="company",default="")
    image = models.ImageField(upload_to="image/%Y/m",default=u"image/default,png",max_length=1000)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

class EmailVertifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=30,verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register",u"注册"),("forget",u"忘记密码")),max_length=10,verbose_name=u"发送类型")
    sendTime = models.DateTimeField(verbose_name="发送时间",default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

class Banner(models.Model):

    title = models.CharField(max_length=100,verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name="轮播图",max_length=100)

    url = models.URLField(max_length=200,verbose_name=u"访问地址")
    index = models.IntegerField(default=100,verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
