import sys, termios, tty

stdinFileDesc = sys.stdin.fileno() #store stdin's file descriptor
oldStdinTtyAttr = termios.tcgetattr(stdinFileDesc) #save stdin's tty attributes so I can reset it later

try:
    print('Press any key to exit...')
    tty.setraw(stdinFileDesc) #set the input mode of stdin so that it gets added to char by char rather than line by line
    sys.stdin.read(1) #read 1 byte from stdin (indicating that a key has been pressed)
finally:
    termios.tcsetattr(stdinFileDesc, termios.TCSADRAIN, oldStdinTtyAttr) #reset stdin to its normal behavior
    print('Goodbye!')
