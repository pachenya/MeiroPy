#
# monster def. file.
#
import mkdat

mdtmp = []
mond = []

class cmond:
  def __init__(self, dname, idx, lev, name, ch, hp, mp, atk, vit, agi, desc = 'Monster.'):
    self.dname = dname
    self.idx = idx
    self.lev = lev
    self.name = str(name)
    self.ch = str(ch)
    self.mhp = int(hp)
    self.mmp = int(mp)
    self.atk = atk
    self.vit = vit
    self.agi = agi
    self.desc = desc
  def DEBUGP(self):
    print(self.dname, self.idx, self.lev, self.name, self.ch, self.mhp, self.mmp, self.atk, self.vit, self.agi, self.desc)

class cmonds:
  def __init__(self):
    menum = mkdat.enuml('data/dat.txt')
    self.mlist = menum.get_elist()
    self.mdat = menum.get_dat()
    self.dat = []
    ldic = {'dname':0, 'lev':1, 'name':2,'ch':3, \
    'hp':4, 'mp':5, 'atk':6, 'vit':7, 'agi':8}
    n = 0
    for i in self.mdat:
      mdtmp = cmond(i[0],i[1],n,i[2],i[3],\
      i[4],i[5],i[6],i[7], i[8])
      # "self.dat"
      self.dat.append(mdtmp)
      n += 1

def test():
  m = cmonds()
  for i in m.dat:
    i.DEBUGP()

# test
# test()

