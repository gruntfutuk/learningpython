import impy
from impy.imp1 import Imp1 as i1
from impy.imp2 import Imp2 as i2

x = i1()
y = i2()

test = input("Text? ")
print(f'{test}')

print(x.imp('Stuart'))
print(y.imp('Clive'))
