#!/usr/bin/python

import os
import time



f = open("all.txt",'r+a')
f.write("hello file")
print(f.readline())
