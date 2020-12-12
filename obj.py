
class COb:
  def __init__(self):
    self.TV  = {'ite':1, 'mod': 2, 'mon':3, 'flo':4}

class CItem(COb):
  def __init__(self, sval, name):
    super(CItem, self).__init__()
    self.tval = self.TV['ite']
    self.sval = sval
    self.name = name

  def printname(self):
    print(self.name)
    print(self.TV['ite'])

class CMondef(COb):
  def __init__(self, ch, name, hp, mp, atk, vit, flags = 0):
    super(CMondef, self).__init__()
    self.ch = ch
    self.name = name
    self.hp = hp
    self.mp = mp
    self.atk = atk
    self.vit = vit
    self.flags = flags
  def printit(self):
    print(self.ch, self.name, self.hp, self.mp)

class CFlg:
  def __init__(self, name, val = 1):
    self.name = name
    self.val = val

#test
#'''
i = CItem(2, 'tanasinn.')
i.printname()

monnames = []
monnames.append('You')
monnames.append('Ghost')
monnames.append('Baka')
mondict = {str(monnames[i]) : i for i in range(len(monnames))}
print(mondict)
flgtmp = []
for i in range(16):
  flgtmp.append(2**i)
for b in flgtmp:
  print(bin(b))
flgname = ['HUMAN', 'UNDEAD', 'FLYING', 'RS_FIRE', \
  'HURT_FIRE']
f = {flgname[i] : flgtmp[i] for i in range(len(flgname))}
print(f)
monds = []
monds.append(CMondef('@', 'You', 15, 15, 8, 8, f['HUMAN'] | f['RS_FIRE']))
for m in monds:
  m.printit()
if monds[0].flags & f['HUMAN']:
  print("It's a human.")
if monds[0].flags & f['FLYING']:
  print("It can fly.")
else:
  print("it cannot fly.")
#'''


