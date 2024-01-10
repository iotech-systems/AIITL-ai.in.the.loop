
from collections import deque


class aiKillMode(object):

   def __init__(self):
      self.modes: deque = deque()
      self.modes.extend(["KILL-CM", "KILL-SM"])

   def next(self) -> str:
      tmp: str = self.modes.popleft()
      self.modes.append(tmp)
      return tmp