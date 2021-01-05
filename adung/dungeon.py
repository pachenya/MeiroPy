#
# adung.py
#
import makemaze
import bres
import curses
from enum import IntEnum, auto
class FL(IntEnum):
  BLO   = auto()
  NONE  = auto()
  DARK  = auto()
  START = auto()
  GOAL  = auto()
  MONST = auto()

class Dung(object):
  def __init__(self, stdscr, MAPW=25, MAPH=21, Z=1):
    self.CAMW = 7
    self.CAMH = 7
    self.MAPW = MAPW
    self.MAPH = MAPH
    self._mx = 1
    self._my = 1
    self.sc = stdscr
    self.grid = [[FL.NONE for j in range(MAPW)] for i in range(MAPH)]
    self.seeg = [[FL.DARK for j in range(MAPW)] for i in range(MAPH)]
    self.Mm = makemaze.MazeMaker(MAPW,MAPH)
    self.Mm.makemz()
    for i in range(MAPH):
      for j in range(MAPW):
        val = self.Mm.getMap(j, i)
        if val == self.Mm.WT_W:
          self.grid[i][j] = FL.BLO
        elif val == self.Mm.WT_N:
          self.grid[i][j] = FL.NONE
        self.seeg[i][j] = FL.DARK
  
  def is_block_xy(self, x, y):
    if x < 0 or x >= self.MAPW or y < 0 or y >= self.MAPH:
      return True
    if self.grid[y][x] == FL.BLO:
      return True
    return False

  def lite_plot_xy(self, x, y):
    if x < 0 or x >= self.MAPW or y < 0 or y >= self.MAPH:
      return
    if self.grid[y][x] == FL.NONE:
      self.seeg[y][x] = FL.NONE
    elif self.grid[y][x] == FL.BLO:
      self.seeg[y][x] = FL.BLO
    return

  def reset_seeg(self):
    for i in range(MAPH):
      for j in range(MAPW):
        self.seeg[i][j] = FL.DARK

  def calc_los_xy(self, px, py):
    length = 3
    for i in range(py-6, py+6):
      for j in range(px-6, px + 6):
        bres.bres2(px, py, j, i, self.lite_plot_xy, self.is_block_xy, length)

  def moveplayer(self, mx, my):
    nx = self._mx + mx
    ny = self._my + my
    if self.is_block_xy(nx, ny):
      return
    self._mx = nx
    self._my = ny
    return

  def putmap_centp_xy(self, x=-2, y=-2):
    self.calc_los_xy(self._mx, self._my)
    if x == -2:
      x = self._mx
    if y == -2:
      y = self._my
    self.sc.clear()
    self.sc.addstr(0,0,'Dungeon')
    camx = x-(self.CAMW)
    camy = y-(self.CAMH)
    for i in range(self.MAPH):
      for j in range(self.MAPW):
        YY = i - camy
        XX = j - camx
        val = self.seeg[i][j]
        ch = '.'
        if i == y and j == x:
          ch = '@'
        elif val == FL.DARK:
          continue
        elif val == FL.BLO:
          ch = '#'
        elif val == FL.NONE:
          ch = '.'
        if XX < 0 or YY < 0 or \
          XX >= self.MAPW or YY >= self.MAPH:
          continue
        self.sc.addstr(YY+1, XX, ch)
    # self.sc.getkey()  

  def DEBUGP(self):
    self.calc_los_xy(self._mx, self._my)
    print(self.seeg)
