#coding:utf-8

from fabric.api import run
from fabric.api import env

host1 = '172.23.7.186'
host2 = "172.23.7.187"
print(type(host1))

p = input("go!:")
print(p)
print(type(p))

env.hosts.extend([host1])
print(env.hosts)
env.user = "root"
env.password = "123456"

def testfun():
    run("hostname")
    run("ls -al")

print("end")