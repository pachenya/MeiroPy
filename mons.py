import mond
import random

class Mons(object):
  def __init__(self, mdef):
    self.mhp = mdef.mhp
    self.mmp = mdef.mmp
    self.hp = self.mhp
    self.mp = self.mmp
    self.ch = mdeef.ch
    self.name = mdef.name
    self.x = 1
    self.y = 1
    self.k = 0
    self.lev = mdef.lev
    self.atk = mdef.atk
    self.vit = mdef.vit
    self.agi = mdef.agi
    self.desc = mdef.desc
  def place(self, mapgridok_xy, x=1,y=1):
    self.x = x
    self.y = y
    self.k = 1
    flag = False
    for i in range(100):
      if not mapgridok_xy(x, y):
        x = random.randint(1,8)
        y = random.randint(1,8)
        continue
      else:
        flag = True
        break
    if flag == False:
      self.k = 0
    return
  def draw(self):
    # Gmain
    return
