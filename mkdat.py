# mkdat.py
#
# To make the list of monsters data and/or skill data.
#
import string

class enuming:
  def __init__(self, n, namekey, ch):
    self.n = n
    self.namekey = namekey
    self.ch = ch
  def DEBUGP(self):
    print(self.n, self.namekey, self.ch)

class enuml:
  def __init__(self, filename):
    f = open(filename, 'r')
    l = f.readlines()
    f.close()
    self.dat = []
    n = 0
    for i in l:
      stch = i[0]
      if stch == '#' or stch == '' or stch == '\n':
        continue
      n += 1
      i = i[:-1]
      stmp = i.split(':')
      ch = '?'
      if len(stmp) >= 2:
        ch = stmp[1]
      else:
        ch = '?'
      d = enuming(n,stmp[0], ch)
      self.dat.append(d)

def test():
  a = enuml('dat.txt')
  for i in a.dat:
    i.DEBUGP()

test()

