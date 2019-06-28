#!/usr/bin/env python3
import sys
import subprocess
if len(sys.argv) > 1:
     name = sys.argv[1]
else:
     name = raw_input('Enter User Name:')
if name == 'root':
   print("Can't do anything with the 'root' user account......Breaking the program")
   sys.exit()

subprocess.call(["adduser", name])
subprocess.call(["usermod", "-aG","wheel", name])
subprocess.call(["passwd", name])
