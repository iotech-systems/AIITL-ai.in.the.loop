
import typing as t
from threading import Lock
from collections import deque


# class aiKillMode(object):
#
#    def __init__(self):
#       self.modes: deque = deque()
#       self.modes.extend(["KILL-CM", "KILL-SM"])
#
#    def next(self) -> str:
#       tmp: str = self.modes.popleft()
#       self.modes.append(tmp)
#       return tmp


class aiModes(object):

   m: [] = ["KILL/CM", "KILL/SM", "SEEK/KILL" "TRK/V0", "TRK/V1", "TRK/V2", "TRK/ONSCR"]

   def __init__(self):
      self.modes: deque = deque()
      self.modes.extend(aiModes.m)

   def next(self) -> str:
      tmp: str = self.modes.popleft()
      self.modes.append(tmp)
      return tmp


class aiTracking(object):

   def __init__(self):
      self.modes: deque = deque()
      self.modes.extend(["TRACK-V0", "TRACK-V1", "TRACK-V2", "ON-SCR-TRACK"])

   def next(self) -> str:
      tmp: str = self.modes.popleft()
      self.modes.append(tmp)
      return tmp


class hbIcons(object):

   icoLock: Lock = Lock()
   okIco: [] = ["O", "*"]
   wrIco: [] = ["?", "!"]
   erIco: [] = ["X", "-"]

   def __init__(self):
      self.icoOK: deque = deque()
      self.icoOK.extend(hbIcons.okIco)
      self.icoWr: deque = deque()
      self.icoWr.extend(hbIcons.wrIco)
      self.icoEr: deque = deque()
      self.icoEr.extend(hbIcons.erIco)
      self.symbols: [] = [self.icoOK, self.icoWr, self.icoEr]

   def next(self, code: 0 = int) -> str:
      try:
         hbIcons.icoLock.acquire()
         sym: str = self.symbols[code].popleft()
         self.symbols[code].append(sym)
         return sym
      except Exception as e:
         print(e)
         return ""
      finally:
         hbIcons.icoLock.release()