#!/usr/bin/env python3
import urllib.request
import os
import subprocess
import string
os.system('sudo apt-get update -y')
os.system('sudo apt-get install pidgin -y')
os.system('sudo apt-get install fusioninventory-agent -y')
s = open("/etc/fusioninventory/agent.cfg").read()
s = s.replace('#server = http://server.domain.com/glpi/plugins/fusioninventory/', 'server = http://backupindia.techblue.co.in/glpi/plugins/fusioninventory/')
f = open("/etc/fusioninventory/agent.cfg", 'w')
f.write(s)
f.close()
os.system('sudo apt install wine64')
os.system('sudo dpkg --add-architecture i386')
os.system('wget -qO- https://dl.winehq.org/wine-builds/winehq.key | sudo apt-key add -')
os.system("sudo apt-add-repository 'deb http://dl.winehq.org/wine-builds/ubuntu/ bionic main'")
os.system('sudo apt-get install --install-recommends winehq-stable')

os.system('sudo mkdir /usr/lib/jvm')
os.chdir('/usr/lib/jvm')
os.system('sudo tar -xvzf /home/tbladmin/jdk-8u202-linux-x64.tar.gz')
x=open("/home/tbladmin/aa.txt", "r")
contents =x.read()
print(contents)
s=open("/etc/profile", "a")
s.write(contents)
x.close()
s.close()

os.system('sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.8.0_202/bin/java" 0')
os.system('sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.8.0_202/bin/javac" 0')
os.system('sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_202/bin/java')
os.system('sudo update-alternatives --set javac /usr/lib/jvm/jdk1.8.0_202/bin/javac')





