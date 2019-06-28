#!/usr/bin/env python3 
N=50
sum=0
count=1

while count <= N:
    sum+=count
    count+=1

avg=float(sum/N)
print(sum)
print("Average is=", avg )


