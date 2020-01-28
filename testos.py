import os, sys, time

with open('spam' , "r") as f:
    default_stdin = os.dup(sys.stdin.fileno())
    os.dup2(f.fileno(), sys.stdin.fileno())
    i = input()
    print(i) # i = 'hello world'
    pid = os.fork()
    print(pid)
    if pid == 0:
        print(11)
        os.execl('/bin/cat','cat', i )
        os.exit()
    elif pid > 0:
        print(3)
        os.wait()
        os.dup2(default_stdin, sys.stdin.fileno())
