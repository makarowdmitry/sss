1. Взять данные для входа из файла построчно
2. Создать файл конфигурацию для текущего сервера
3. Выполнить команды все
4. Залить файл
5. reboot
6. Удалить файл конфигурации

7. Проверить все прокси по окончанию на чек
8. Сохранить рабочие в нужно формате для загрузки.

https://github.com/paramiko/paramiko


3proxy-0.7.1.2.tgz sources for Unix/Linux/Windows and documentation http://3proxy.ru/download

================== Установка 3proxy-0.6.1.tgz ======================
passwd
service iptables stop
service iptables save
chkconfig iptables off
cd /usr/local/src
yum update -y
yum install -y mc nano gcc make
wget http://3proxy.ru/0.6.1/3proxy-0.6.1.tgz
tar -xvzf 3proxy-0.6.1.tgz
cd 3proxy-0.6.1
make -f Makefile.Linux
mkdir /usr/local/etc/3proxy
mkdir /usr/local/etc/3proxy/bin
mkdir /usr/local/etc/3proxy/logs
mkdir /usr/local/etc/3proxy/stat
cp src/3proxy /usr/local/etc/3proxy/bin
cp ./scripts/rc.d/proxy.sh /etc/init.d/3proxy
chkconfig 3proxy on
touch /usr/local/etc/3proxy/3proxy.cfg
cd /usr/local/etc/3proxy
nano 3proxy.cfg


cp /root/usr/local/src/3proxy-0.6.1/src/3proxy /usr/local/etc/3proxy/bin

/usr/local/src/3proxy-0.6.1/src/3proxy
f9W6_lSPAO1QS_
----------------------------------------------------------
daemon
auth strong
users admin:CL:12345
users vasya:CL:123456
socks -n -a -p3128 -i185.20.225.70 -e185.20.225.70
flush
allow admin,vasya
----------------— Ctrl + x —— y —-— Enter —---------------

/usr/local/etc/3proxy/bin/3proxy /usr/local/etc/3proxy/3proxy.cfg
reboot