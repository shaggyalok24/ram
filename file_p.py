#!/usr/bin/env python3
import os
f=open("aa.txt", "r")
contents =f.read()
print(contents)

s=open("/etc/profile", "a")
s.write(contents)
f.close()
s.close()
