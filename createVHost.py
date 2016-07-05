#coding:utf8
import os
print "                       <虚拟主机设置向导>"
print ""
print '运行前请确保在Apache主配置文件（一般为/etc/httpd/conf/httpd.conf）内包含虚拟主机目录,如“Include conf/extra/*.conf”' ########################这个很重要，不然不生效。
print ""
raw_input("请按<Enter>键开始>>")
#########################################【请先设置常用固定选项】##########################################
WwwRoot='/var/www/' #网站根目录
ApacheRoot='/etc/httpd/' #Apache程序目录
ConfRoot='/etc/httpd/conf/httpd.conf' #Apache主配置文件
VirtualHostRoot='/etc/httpd/conf/extra/' #Apache虚拟主机配置文件目录
LogRoot='/etc/httpd/logs/' #Apache日志目录
ApacheUseGroup='apache:apache' #Apache用户和用户组（user:group）
WebMaster='website@1daor.com' #管理员邮箱
############################################【常用设置完毕】###############################################
ServerName=''
while ServerName=='':
    ServerName=raw_input('请输入域名（必填项）：') 
print '您输入的域名为：'+ServerName 
n=0
ServerAilas=[] 
ailas=raw_input('若还需绑定其他域名，请在此输入，不需绑定的话直接按<Enter>：')
ServerAilas.append(ailas) 
while ServerAilas[n]!='': 
    n=n+1
    ailas=raw_input('若还需绑定其他域名，请在此输入，不需绑定的话直接按<Enter>：')
    ServerAilas.append(ailas)
del ServerAilas[n] 
if n!=0:
    print '您输入了以下的别名：'
for i in range(len(ServerAilas)):
    print ServerAilas[i]
ServerAdmin=raw_input('请输入网站管理员邮箱，按回车直接使用<'+WebMaster+'>：') or WebMaster 
print '管理员邮箱为：'+ServerAdmin 
DocumentRoot=raw_input('请输入网站目录，按回车直接使用<'+WwwRoot+ServerName+'>：') or WwwRoot+ServerName
print '网站目录为：'+DocumentRoot
ErrorLogT=raw_input('是否记录错误日志,按<Enter>记录[Y/N]：')
if ErrorLogT=='y' or ErrorLogT=='Y' or ErrorLogT=='':
    ErrorLog=raw_input('请输入日志路径，按<Enter>使用'+LogRoot+ServerName+'_error.log：') or LogRoot+ServerName+'_error.log'
    print '您选择的错误日志路径为'+ErrorLog 
else:
    print '您选择不开启错误日志'
CustomLogT=raw_input('是否记录访问日志,按<Enter>记录[Y/N]：')
if CustomLogT=='y' or CustomLogT=='Y' or CustomLogT=='':
    CustomLog=raw_input('请输入日志路径，按<Enter>使用'+LogRoot+ServerName+'_access.log：') or LogRoot+ServerName+'_access.log'
    print '您选择的错误日志路径为'+CustomLog 
else:
    print '您选择不开启访问日志'
VirtualHostConf=VirtualHostRoot+ServerName 
if os.path.exists(VirtualHostConf)==False:
    f=open(VirtualHostConf,'w')
    f.write('<VirtuaHost *.80>'+os.linesep)
    f.write('ServerAdmin '+ServerAdmin+os.linesep)
    f.write('DocumentRoot '+DocumentRoot+os.linesep)
    f.write('ServerName '+ServerName+os.linusep)
    if n!=0:
        for i in range(len(ServerAilas)):
            f.write('ServerAilas '+ServerAilas[i]+os.linesep)
    if ErrorLog_=='y'or'Y'or'':
        f.write('ErrorLog '+ErrorLog+os.linesep)
    else:
        f.write('#ErrorLog '+ErrorLog+os.linesep)
    if CustomLog_=='y'or'Y'or'':
        f.write('CustomLog '+CustomLog+os.linesep) 
    else:
        f.write('#CustomLog '+CustomLog+os.linesep)
    f.write('</VirtualHost>') 
    f.close()
if os.path.exists(VirtualHostConf)==Ture:
    print '目录下已有同名配置文件'
    b=raw_input('显示文件内容请选择[Y]，否则按<Enter>：')
    if b=='Y'or'y':
        f=open(VirtualHostConf,'r')
        line=f.readline()
        while line:
            print line
            line=f.readline()
        f.close()
        exit()
    else:
        exit()
os.mkdir(DocumentRoot)
os.popen('chown -R '+ApacheUseGroup)
cmd=os.popen('service apache reload')
print cmd.read()
f=open(VirtualHostConf,'r')
line=f.readline()
while line:
    print line
    line=f.readline()
f.close()
exit()



