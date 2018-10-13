# Vacation
基于django框架开发的假期学生离校登记系统<br/>

## 使用方法：</br>
1.下载代码到本地</br>
2.cd到项目目录</br>
3.进行数据库迁移，执行</br>
```
python manage.py makemigrations
python manage.py migrate
```
4.创建django自带后端管理admin的账号</br>
```
python manage.py createsuperuser
```
按照要求设置账号，邮箱，密码，输入密码时不会显示字符</br>
5.启动项目，执行</br>
```
python manage.py runserver 0.0.0.0:8000
```
6.进入admin管理界面，在浏览器中输入
```
http://127.0.0.1:8000/admin/
```
或者</br>
```
http://服务器ip:8000/admin/
```
7.在user表中添加老师等需要查看学生登记信息的管理员的账户</br>
8.在statistics表中安装院系，年级，节假日及其在校人数添加相应数据</br>
9.配置完成</br>
</br>
学生登记网址：</br>
```
http://127.0.0.1:8000/index/
```
教师查看登记情况网址：</br>
```
http://127.0.0.1:8000/leaveschooltlist/
```
