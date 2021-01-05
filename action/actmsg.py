from enum import Enum, auto
class Acts(Enum):
  ACT_NONE = auto()
  ACT_HIT = auto()
  ACT_KICK = auto()
  ACT_SLASH = auto()
  ACT_SCRAC = auto()
  ACT_BITE = auto()
  ACT_TOUCH = auto()
  ACT_PICKUP = auto()

def amsg(A, B, act):
  # aes = ('s','ss','o','x','ch','sh')
  rval = 'hits'
  if act == Acts.ACT_NONE:
    rval = 'does nothing to'
  elif act == Acts.ACT_HIT:
    rval = 'hits'
  elif act == Acts.ACT_KICK:
    rval = 'kicks'
  elif act == Acts.ACT_SLASH:
    rval = 'slashes'
  elif act == Acts.ACT_SCRAC:
    rval = 'scraches'
  elif act == Acts.ACT_BITE:
    rval = 'bites'
  elif act == Acts.ACT_TOUCH:
    rval = 'touches'
  elif act == Acts.ACT_PICKUP:
    rval = 'picks up'

  stmp = str(A)+' '+rval+' '+str(B)+'.'
  return stmp
