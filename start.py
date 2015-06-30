# coding: utf8
#! /usr/bin/env python

# import paramiko #, base64
# 1. формируем файл скрипта
# 2. заливаем его на сервер и исполняем
# 3. Чекаем все прокси

import os

PROXY_USER = "goemailgo"
PROXY_PASS ="q8uir"

def create_script_install_proxy(ip,pr_user,pr_pass):
	create_file = open('install_socks.py','w')
	python_file = '''#! /usr/bin/env python
import os

# a = os.system("""
# 	service iptables stop
# 	service iptables save
# 	chkconfig iptables off
# 	cd /usr/local/src
# 	yum update -y
# 	yum install -y mc nano gcc make
# 	wget http://3proxy.ru/0.6.1/3proxy-0.6.1.tgz
# 	tar -xvzf 3proxy-0.6.1.tgz
# 	cd 3proxy-0.6.1
# 	make -f Makefile.Linux
# 	mkdir /usr/local/etc/3proxy
# 	mkdir /usr/local/etc/3proxy/bin
# 	mkdir /usr/local/etc/3proxy/logs
# 	mkdir /usr/local/etc/3proxy/stat
# 	cp src/3proxy /usr/local/etc/3proxy/bin
# 	cp ./scripts/rc.d/proxy.sh /etc/init.d/3proxy
# 	chkconfig 3proxy on
# 	""")


def create_conf_proxy(ip_serv,login_proxy,pass_proxy):
	os.chdir("/home/tp")
	proxy_conf = """daemon
auth strong
users """+login_proxy+":CL:"+pass_proxy+"""
socks -n -a -p3128 -i"""+ip_serv+" -e"+ip_serv+"""
flush
allow """+login_proxy+"""
	"""
	conf_proxy_create = open("3proxy.cfg","w")
	conf_proxy_create.writelines(proxy_conf)
	conf_proxy_create.close()
	return "ok"

create_conf_proxy("'''+str(ip)+'","'+str(pr_user)+'","'+str(pr_pass)+'''")
'''
	create_file.writelines(python_file)
	create_file.close()



data_vps = open('data_vps.txt','r').readlines()

for vps in data_vps:
	vps_lst = vps.split(',')
	create_script_install_proxy(vps_lst[0],PROXY_USER,PROXY_PASS)
	'''Подключиться к ssh. Установить python. Залить скрипт python. Исполнить. Отключиться.

	'''

	os.system('python install_socks.py')
	os.remove('install_socks.py')

# a = os.system("""
# 	service iptables stop
# 	service iptables save
# 	chkconfig iptables off
# 	cd /usr/local/src
# 	yum update -y
# 	yum install -y mc nano gcc make
# 	wget http://3proxy.ru/0.6.1/3proxy-0.6.1.tgz
# 	tar -xvzf 3proxy-0.6.1.tgz
# 	cd 3proxy-0.6.1
# 	make -f Makefile.Linux
# 	mkdir /usr/local/etc/3proxy
# 	mkdir /usr/local/etc/3proxy/bin
# 	mkdir /usr/local/etc/3proxy/logs
# 	mkdir /usr/local/etc/3proxy/stat
# 	cp src/3proxy /usr/local/etc/3proxy/bin
# 	cp ./scripts/rc.d/proxy.sh /etc/init.d/3proxy
# 	chkconfig 3proxy on
# 	""")


# def create_conf_proxy(ip_serv,login_proxy,pass_proxy):
# 	os.chdir("/home/tp")
# 	proxy_conf = """daemon
# auth strong
# users """+login_proxy+":CL:"+pass_proxy+"""
# socks -n -a -p3128 -i"""+ip_serv+" -e"+ip_serv+"""
# flush
# allow """+login_proxy+"""
# 	"""
# 	conf_proxy_create = open('3proxy.cfg','w')
# 	conf_proxy_create.writelines(proxy_conf)
# 	conf_proxy_create.close()
# 	return "ok"

# create_conf_proxy(ip,"goemailgo",)

# # print proxy_conf










	# key = paramiko.RSAKey(data=base64.decodestring('AAA...'))
	# client = paramiko.SSHClient()
	# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	# client.connect(vps_lst[0], username=vps_lst[1], password=vps_lst[2])
	# chan = client.invoke_shell()
	# chan.send('ls -l')
	# print chan.recv(1024)
	

	# now, connect and use paramiko Transport to negotiate SSH2 across the connection
	# try:
	# t = paramiko.Transport((hostname, Port))
	# t.connect(hostkey, username, password, gss_host=socket.getfqdn(hostname),
	# gss_auth=UseGSSAPI, gss_kex=DoGSSAPIKeyExchange)
	# sftp = paramiko.SFTPClient.from_transport(t)
	# # dirlist on remote host
	# dirlist = sftp.listdir('.')
	# print("Dirlist: %s" % dirlist)
	# # copy this demo onto the server
	# try:
	# sftp.mkdir("demo_sftp_folder")
	# except IOError:
	# print('(assuming demo_sftp_folder/ already exists)')
	# with sftp.open('demo_sftp_folder/README', 'w') as f:
	# f.write('This was created by demo_sftp.py.\n')
	# with open('demo_sftp.py', 'r') as f:
	# data = f.read()
	# sftp.open('demo_sftp_folder/demo_sftp.py', 'w').write(data)
	# print('created demo_sftp_folder/ on the server')
	# # copy the README back here
	# with sftp.open('demo_sftp_folder/README', 'r') as f:
	# data = f.read()
	# with open('README_demo_sftp', 'w') as f:
	# f.write(data)
	# print('copied README back here')
	# # BETTER: use the get() and put() methods
	# sftp.put('demo_sftp.py', 'demo_sftp_folder/demo_sftp.py')
	# sftp.get('demo_sftp_folder/README', 'README_demo_sftp')
	# t.close()

	# stdin, stdout, stderr = client.exec_command('cd /usr','pwd')
	# stdin, stdout, stderr = client.exec_command('pwd')
	
	# for line in stdout:
	# 	print '... ' + line.strip('\n')
	# client.close()



 



