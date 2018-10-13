# Vacation
基于django框架开发的假期学生离校登记系统

使用方法：
1.下载代码到本地
2.cd到项目目录
3.进行数据库迁移，执行
python manage.py makemigrations
python manage.py migrate
4.创建django自带后端管理admin的账号
python manage.py createsuperuser
按照要求设置账号，邮箱，密码，输入密码时不会显示字符
5.启动项目，执行
python manage.py runserver
