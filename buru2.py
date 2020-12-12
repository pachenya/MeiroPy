import curses
from bres import bres2
import makemaze
import random

stdscr = curses.initscr()
curses.noecho()

F_NONE   = 1 
F_BLO    = 2
F_PLAYER = 4
F_DARK   = 5
CAMW = 7
CAMH = 7
H = 21 
W = 21

stdscr.clear()
stdscr.addstr(1, 2, 'Welcome to the world!')
stdscr.refresh()
stdscr.getch()

grid = [[F_NONE for i in range(W)] for j in range(H)]
seeg = [[F_DARK for i in range(W)] for j in range(H)]

Mm = makemaze.MazeMaker(W, H)

Mm.makemz()

for i in range(H):
  for j in range(W):
    val = Mm.getMap(j, i)
    if val == Mm.WT_W:
      grid[i][j] = F_BLO
    elif val == Mm.WT_N:
      grid[i][j] = F_NONE

def block_xy(x,y):
  global grid
  if x < 0 or y < 0 or x >= W or y >= H:
    return True
  if grid[y][x] == F_BLO:
    return True
  return False

def plot_xy(x,y):
  global grid, seeg
  if x < 0 or y < 0 or x >= W or y >= H:
    return
  if grid[y][x] == F_BLO:
    seeg[y][x] = F_BLO
  elif grid[y][x] == F_NONE:
    seeg[y][x] = F_NONE
  else:
    seeg[y][x] = F_DARK

def clear_seeg():
  for i in range(H):
    for j in range(W):
      seeg[i][j] = F_DARK

px = 1
py = 1

grid[py][px] = F_NONE 

def putmap_aux(x, y, val):
  ch = ' '
  if val == F_NONE:
    ch = '.'
  elif val == F_BLO:
    ch = '#'
  elif val == F_PLAYER:
    ch = '@'
  elif val == F_DARK:
    ch = ' '
  stdscr.addstr(y, x, ch)

def putmap(flag):
  for i in range(H):
    for j in range(W):
      val = F_NONE
      if flag == True:
        val = seeg[i][j]
      else:
        val = grid[i][j]
      if py == i and px == j:
        val = F_PLAYER
      putmap_aux(j, i+1, val)

def putmap_centp_xy(x, y):
  camx = x-(CAMW)
  camy = y-(CAMH)
  for i in range(H):
    for j in range(W):
      YY = i - camy
      XX = j - camx
      val = seeg[i][j]
      if i == y and j == x:
        val = F_PLAYER
      if XX < 0 or YY < 0 or XX >= W or YY >= H:
        continue
      putmap_aux(XX, YY+1, val)

stdscr.clear()
putmap(False)
stdscr.getch()

def okcancel(word):
  stdscr.addstr(0,0,word)
  key = stdscr.getkey()
  if key == 'o':
    return True
  elif key == 'c':
    return False
  return False
  
done = False
while(not done):
  mx = 0
  my = 0
  clear_seeg()
  for i in range(H + 20):
    for j in range(W + 20):
      bres2(px, py, j-10, i-10, plot_xy, block_xy, 7)
  stdscr.clear()
  putmap_centp_xy(px,py)
  # putmap(True)
  key = stdscr.getkey()
  if key == 'Q':
    if okcancel('Realy quit? (o or c)'):
      done = True
      break
    else:
      continue

  if key == 'd' or key == 'l':
    mx = 1
  elif key == 'a' or key == 'h':
    mx = -1
  elif key == 'x' or key == 'j':
    my = 1
  elif key == 'w' or key == 'k':
    my = -1
  elif key == 'd' or key == 'l':
    mx = 1
  elif key == 'q' or key == 'y':
    mx = -1
    my = -1
  elif key == 'e' or key == 'u':
    mx = 1
    my = -1
  elif key == 'z' or key == 'b':
    mx = -1
    my = 1
  elif key == 'c' or key == 'n':
    mx = 1
    my = 1
  else:
    continue

  nx = px + mx
  ny = py + my
  if nx < 0 or nx >= W or ny < 0 or ny >= H:
    continue
  elif grid[ny][nx] == F_NONE:
    px = nx
    py = ny

curses.echo()
curses.endwin()

