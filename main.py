import curses
# import makemaze
from action import actmsg
from adung.dungeon import Dung
import random

def main():
  stdscr = curses.initscr()
  curses.noecho()
  stdscr.clear()
  s = actmsg.amsg('The cat','the lazy dog', \
  actmsg.Acts.ACT_SCRAC)
  stdscr.addstr(1, 2, s)
  stdscr.getkey()
  stdscr.clear()
  stdscr.addstr(2, 2, ' -- MeiroPy --')
  stdscr.addstr(5, 2, '[Press any key]')
  stdscr.getkey()
  du = Dung(stdscr)
  # du.DEBUGP()
  stdscr.getkey()
  while True:
    du.putmap_centp_xy()
    ch = stdscr.getkey()
    mx = 0
    my = 0
    if ch == 'w':
      my = -1
    elif ch == 'x':
      my = 1
    elif ch == 'a':
      mx = -1
    elif ch == 'd':
      mx = 1
    elif ch == 'Q':
      stdscr.addstr(0,0,'See Yah!')
      stdscr.getkey()
      break
    if my != 0 or mx != 0:
      du.moveplayer(mx, my)
  return

if __name__ == '__main__':
  try:
    main()
  finally:
    curses.echo()
    curses.endwin()
