from django.shortcuts import render,redirect
from . import  models
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse


# Create your views here.
GRADE = {
        '1': '2015',
        '2': '2016',
        '3': '2017',
        '4': '2018',
}
CLASSIFY = {
    '1': '元旦',
    '2': '五一',
    '3': '国庆',
}

#学生离校登记
def index(request):
    if request.method == 'POST':
        schoolnumber = request.POST.get('schoolnumber', '未输入')
        stusystem=request.POST.get('stusystem', '未输入')
        stuname = request.POST.get('stuname', '未输入')
        sex = request.POST.get('sex', '无')
        stugrade = request.POST.get('stugrade', 2)
        stuclass = request.POST.get('stuclass', '未输入')
        stunation = request.POST.get('stunation', '未输入')
        stuaddress = request.POST.get('stuaddress', '未输入ַ')
        studirection = request.POST.get('studirection', '未输入')
        leavetime = request.POST.get('leavetime', '1997-01-01')
        cometime = request.POST.get('cometime', '1997-01-01')
        stuphone = request.POST.get('stuphone', '未输入')
        teacher = request.POST.get('teacher', '未输入')
        teacherphone = request.POST.get('teacherphone', '未输入')
        classify = request.POST.get('classify', 3),
        new_leaveschool = models.leaveschool(
            schoolnumber = schoolnumber,
            stusystem = stusystem,
            stuname = stuname,
            sex = sex,
            stugrade = stugrade[0],
            stuclass = stuclass,
            stunation = stunation,
            stuaddress = stuaddress,
            studirection = studirection,
            leavetime = leavetime,
            cometime = cometime,
            stuphone = stuphone,
            teacher = teacher,
            teacherphone = teacherphone,
            classify = classify[0],
        )
        new_leaveschool.save()
        try:
            cnt = models.statistics.objects.get(sgrade=stugrade[0], ssystem=stusystem, sclassify=classify[0], )
        except:
            cnt = None
        if cnt:
            cnt.ssum += 1
            cnt.save()
        else:
            print('请完善statistics表！！！缺少的数据的值：年级=%s,院系=%s,假期=%s' % (GRADE[stugrade[0]], stusystem, CLASSIFY[classify[0]]))
        return HttpResponse('提交成功!!!')
    else:
        return render(request, 'leaveschoolregistration/index.html')

#管理员登录
def login(request):
    if request.method == 'POST':
        accountnum = request.POST.get("user")
        pwd=request.POST.get("pwd")
        try:
            user = models.user.objects.get(accountnum=accountnum)
        except:
            user = None
        if user:
            if pwd == user.password:
                request.session['has_loged'] = True
                request.session.set_expiry(12000)
                return render(request, 'leaveschoolregistration/loginsuccess.html')
            else:
                del request.session['has_loged']
                return render(request,'leaveschoolregistration/login.html',{'error':'密码错误'})
        else:
            return  render(request,'leaveschoolregistration/login.html',{'error':'用户不存在'})
    elif request.method == 'GET':
        return render(request,'leaveschoolregistration/login.html')

#查询学生登记列表
def leaveschooltlist(request):
    if request.method == 'POST':
        if request.session.get('has_loged', False)==True:
            q = {}
            stusystem = request.POST.get('stusystem', '-1')
            stunation = request.POST.get('stunation', '-1')
            classify = request.POST.get('classify', 3),
            stugrade = request.POST.get('stugrade',2),
            if stusystem != '-1':
                q['stusystem'] = stusystem
            if stunation != '-1':
                q['stunation'] = stunation
            q['classify'] = classify[0]
            q['stugrade'] = stugrade[0]
            querylist = models.leaveschool.objects.filter(**q).order_by("schoolnumber")
            querylist.query.group_by = ['stuclass']
            vacation =CLASSIFY[classify[0]]
            grade = GRADE[stugrade[0]]
            p={}
            if stusystem!='-1':
                p['ssystem'] = stusystem
            p['sclassify'] = classify[0]
            p['sgrade'] = stugrade[0]
            x = 0
            finisher = 0
            try:
                cnt = models.statistics.objects.filter(**p)
            except:
                cnt = None
            if cnt:
                for i in cnt:
                    x += i.stotal
                    finisher += i.ssum
            else:
                print('请完善statistics表！！！缺少的数据的值：年级=%s,院系=%s,假期=%s' %(GRADE[stugrade[0]], stusystem, CLASSIFY[classify[0]]))
            remainder = x - finisher
            if stusystem=='-1':
                stusystem='全校'
            return render(request,'leaveschoolregistration/leavelist.html',{'querylist':querylist,'finisher':finisher,'remainder':remainder,'stusystem':stusystem,'grade':grade,'vacation':vacation})
        else:
           return render(request,'leaveschoolregistration/loginfail.html')
    else:
        return render(request, 'leaveschoolregistration/query.html')

