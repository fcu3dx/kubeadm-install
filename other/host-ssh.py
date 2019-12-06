import os

for i in range (191,200):
    # ssh -t 172.17.0.i -o StrictHostKeyChecking=no "ls"
    shell = "ssh -t 172.17.0.{} -o StrictHostKeyChecking=no 'ls'".format(i)
    print(shell)
    os.system(shell)