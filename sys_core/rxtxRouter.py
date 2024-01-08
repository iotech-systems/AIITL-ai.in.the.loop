import time

import serial as ser
import threading as th
import configparser as cp
# -- -- -- --
from sys_core.utils import utils
from sys_core.rxtxPipeQ import rxtxPipeQ


class rxtxRouter(object):

   def __init__(self, ini: cp.ConfigParser):
      self.ini: cp.ConfigParser = ini
      self.ini_sec: cp.SectionProxy = self.ini["RXTX_PIPES"]
      self.pipes_arr: [] = None
      self.rxtx_pqs: [rxtxPipeQ] = []
      self.router_thread: th.Thread = th.Thread(target=self.__router_thread)

   def load_ini(self) -> int:
      try:
         tmp: str = self.ini_sec["PIPES"]
         print(tmp)
         if tmp in ["", None]:
            pass
         self.pipes_arr = tmp.split("\n")
         self.rxtx_pqs = [rxtxPipeQ(pipe_str=pstr) for pstr in self.pipes_arr]
         return 0
      except Exception as e:
         utils.log_err(e)
         return 1
      finally:
         pass

   def start(self) -> int:
      self.router_thread.start()
      for rxtx_item in self.rxtx_pqs:
         rxtx_item.init()
         rxtx_item.start()
      return 0

   def stop(self) -> int:
      return 0

   def __router_thread(self):
      rxtx_air: rxtxPipeQ = [i for i in self.rxtx_pqs if i.qtag == "AIR_RXTX"][0]
      rxtx_fc: rxtxPipeQ = [i for i in self.rxtx_pqs if i.qtag == "FC_RXTX"][0]
      print([rxtx_air, rxtx_fc])
      while True:
         try:
            # read air
            # if self.rxtx_pqs
            time.sleep(2.0)
         except Exception as e:
            utils.log_err(e)
         finally:
            pass

