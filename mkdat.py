# mkdat.py
#
# To make the list of monsters data.
#
import string

class enuming:
  def __init__(self, n, namekey, ch='?'):
    self.n = int(n)
    self.namekey = str(namekey)
    self.ch = ch = str(ch)
  def DEBUGP(self):
    print(self.n, self.namekey, self.ch)

class enuml:
  def __init__(self, filename, debugmode=False):
    f = open(filename, 'r')
    l = f.readlines()
    f.close()
    self.dat = []
    self.elist = []
    n = 0
    for i in l:
      stch = i[0]
      if stch == '#' or stch == '' or stch == '\n':
        continue
      n += 1
      i = i[:-1]
      stmp = i.split(':')
      
      if debugmode:
        for s in stmp:
          print(s, end=',')
        print(' : len ->' + str(len(stmp)))
      
      ch = '?'
      if len(stmp) >= 2:
        ch = stmp[1]
      else:
        ch = '?'
      d = enuming(n,stmp[0], ch)
      self.elist.append(d)
      self.dat.append(stmp)
  def get_elist(self):
    return self.elist
  def get_dat(self):
    return self.dat

def test():
  a = enuml('data/dat.txt')
  for i in a.elist:
    i.DEBUGP()

def test2():
  a = enuml('data/dat.txt')

test()
test2()


