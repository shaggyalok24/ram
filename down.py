#!/usr/bin/env python3
import urllib.request
import os
import subprocess
urllib.request.urlretrieve('https://community.jaspersoft.com/modal_forms/nojs/jf-user-login-register?optoutdest=https://sourceforge.net/projects/jasperstudio/files/JaspersoftStudio-6.8.0/TIB_js-studiocomm_6.8.0_linux_amd64.deb/download', 'jsp.deb')
os.system('sudo gdebi jsp.deb')
