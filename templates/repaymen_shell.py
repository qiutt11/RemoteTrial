#代码拼写字符串，时间可以从前台选择，也可以new date对象生成一个   拼好字符串执行process p=Runtime.getRuntime().exec("这里写 shell 命令")
# _*_ coding: utf-8 _*_
import os,sys
import paramiko
#服务器相关信息，下面输入用户名、密码、ip等信息
ip = "10.100.19.88"
port = 22
user = "hcadmin"
password = "123456"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#建立连接
ssh.connect(ip,port,user,password,timeout = 10)
#输入 linux命令
#stdin,stdout,stderr =ssh.exec_command("pwd")
stdin,stdout,stderr =ssh.exec_command("su root")
stdin,stdout,stderr =ssh.exec_command("kaka@!#123")
stdin,stdout,stderr =ssh.exec_command("who")
# stdin,stdout,stderr =ssh.exec_command("pwd")
# stdin,stdout,stderr =ssh.exec_command("./helloWorld.py")
#输入命令执行结果
result = stdout.read()
print (result)
#关闭连接
ssh.close()

