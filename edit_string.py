import curses
import os
from string import printable

def prompt(ps=None, value=''):
   scr = curses.initscr()
    if ps is None:
        ps = ': '
    height, width = scr.stdscr.getmaxyx()
    scr.stdscr.addstr(scr.top_lines + 1, 0, ' ' + ps, palette.PROMPT)
    editwin = curses.newwin(1, width - len(ps) - 1, scr.top_lines + 1,
                            len(ps) + 1)
    from curses.textpad import Textbox
    show_cursor()
    editwin.addstr(0, 0, str(value))
    box = Textbox(editwin, insert_mode=True)
    scr.stdscr.refresh()
    box.edit(enter_is_terminate)
    result = box.gather().rstrip()
    hide_cursor()
    scr.stdscr.move(scr.top_lines + 1, 0)
    scr.stdscr.clrtoeol()
    scr.stdscr.refresh()
    return result 

def edit_string(win, editable):
   pos = 0
   win.nodelay(True)
   key=""
   win.clear()                
   win.addstr(editable)
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
         win.addstr(editable) 
         if key == os.linesep:
            return editable          
      except Exception:
         pass         

editable = 'Mary had a little lamb'
#result = curses.wrapper(edit_string,editable)
#print(f'result: {result}')
prompt()