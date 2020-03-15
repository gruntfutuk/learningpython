import curses
import os
from string import printable


def edit_string(win, editable):
   pos = 0
   win.nodelay(True)
   key=""
   win.clear()                
   win.addstr(f"000{editable}") 
   while True:          
      try:                 
         key = win.getkey()
         if key in printable:
            editable = f'{editable[:pos]}{key}{editable[pos+1:]}'
         elif key == curses.KEY_LEFT and pos > 0:
            pos -= 1
         elif ord(key) == curses.KEY_RIGHT and pos < (len(editable) - 1):
            pos += 1
         win.clear()                
         win.addstr(f"{ord(key):3}{editable}") 
         if key == os.linesep:
            return editable          
      except Exception:
         pass         

editable = 'Mary had a little lamb'
result = curses.wrapper(edit_string,editable)
print(f'result: {result}')