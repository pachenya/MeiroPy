import copy

class ctest(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

class cchotest(ctest):
  def __init__(self, x, y, z):
    super().__init__(x, y)
    self.z = z
  def copy(self):
    return copy.deepcopy(self)

def test():
  a = ctest(1,2)
  b = cchotest(3,4,5)
  print(a.x, a.y)
  print(b.x, b.y, b.z)
  c = b.copy()
  c.z = 9
  print(c.x, c.y, c.z)

#'''
test()
#'''
