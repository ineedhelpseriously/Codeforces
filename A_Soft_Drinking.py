import sys

n,k,l,c,d,p,nl,np=map(int,sys.stdin.readline().split())
x=(k*l)//nl
y=c*d
z=p//np

sys.stdout.write(str(int(min(x,y,z)//n)))