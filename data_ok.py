# coding: utf8
# 1. Считываем файл
# 2. Создать регулярное выражение, которое ищет ip
# 3. Создать регулярное выражение, которое ищет пароль (Указать после какой строки стоит пароль)
# 4. Определить что стояло в файле ваше по позиции ip или пароль и в зависимости от этого сформировать список словарей
# 5. [{'ip':ip, 'pass', pass}]
# 6. убрать дубликаты
# 7. Записать данные в файл data_socks

import re

STR_PASS = r'Root pass:'
STR_USER = 'root'

file_read = open('raw_vps.txt','r').read()
ip4_re = r'[0-9]+(?:\.[0-9]+){3}'
pass_re = STR_PASS+r'\s+(?P<pass>\S+)\s+'

list_ip_search = re.findall(ip4_re, file_read)
list_pass_search = re.findall(pass_re, file_read)

index_ip4 = file_read.index(list_ip_search[0])
index_pass = file_read.index(list_pass_search[0])


if len(list_ip_search) != len(list_pass_search):
	print 'К каждому ip должен быть пароль'
else:
	list_vps = []
	for ip in list_ip_search:
		dict_this = {'ip':ip}
		list_vps.append(dict_this)
	for i,l in enumerate(list_vps):
		l['pass'] = list_pass_search[i]
	for i in list_vps:
		save_file = open('data_vps.txt','a')
		str_save = i['ip']+','+STR_USER+','+i['pass']+'\n'
		save_file.write(str_save)
		save_file.close()



