from django.db import models

# Create your models here.
#学生登记表
class leaveschool(models.Model):
    GRADE = (
        (1, '2015'),
        (2, '2016'),
        (3, '2017'),
        (4, '2018'),
    )
    CLASSIFY = (
        (1, '元旦'),
        (2, '五一'),
        (3, '国庆'),
    )
    schoolnumber = models.CharField(max_length=20,default='暂无',verbose_name="学号")
    stusystem = models.CharField(max_length=20,default='暂无',verbose_name="院系")
    stuname = models.CharField(max_length=10,default='暂无',verbose_name="姓名")
    sex = models.CharField(max_length=3,default='男',verbose_name="性别")
    stuclass = models.CharField(max_length=40,default='暂无',verbose_name="班级")
    stunation = models.CharField(max_length=10,default='暂无',verbose_name="名族")
    stuaddress = models.CharField(max_length=20,default='暂无',verbose_name="生源地")
    studirection = models.CharField(max_length=20,default='暂无',verbose_name="去向")
    leavetime = models.DateField(null=False,default='2018-08-15',verbose_name="离校日期")
    cometime = models.DateField(null=False,default='2018-08-15',verbose_name="归校日期")
    stuphone = models.CharField(max_length=20,default='暂无',verbose_name="联系电话")
    teacher = models.CharField(max_length=10, default='暂无',verbose_name="辅导员")
    teacherphone = models.CharField(max_length=20,default='暂无',verbose_name="辅导员电话")
    classify = models.IntegerField(default=3,choices=CLASSIFY,verbose_name="假期")
    stugrade = models.IntegerField(choices=GRADE, default=2,verbose_name="年级")


    def __str__(self):  #python2.0替换为def __unicode__(self)
        return self.stuname

#登记情况统计表
class statistics(models.Model):
    GRADE = (
        (1, '2015'),
        (2, '2016'),
        (3, '2017'),
        (4, '2018'),
    )
    CLASSIFY = (
        (1, '元旦'),
        (2, '五一'),
        (3, '国庆'),
    )
    sgrade = models.IntegerField(choices=GRADE,default=2,verbose_name="年级")
    ssystem = models.CharField(max_length=20,default='暂无',verbose_name="院系")
    stotal = models.IntegerField(default=100,verbose_name="总人数")
    ssum = models.IntegerField(default=0,verbose_name="已登记人数")
    sclassify = models.IntegerField(default=3,choices=CLASSIFY,verbose_name="假期")

    def __str__(self):  #python2.0替换为def __unicode__(self)
        return self.ssystem

#管理员表
class user(models.Model):
    username = models.CharField(max_length=20, default='暂无',verbose_name="名称")
    accountnum = models.CharField(max_length=20, default='暂无',verbose_name="账号")
    password = models.CharField(max_length=20, default='暂无',verbose_name="密码")
