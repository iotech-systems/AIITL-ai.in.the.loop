

class sysColors(object):
   red = (255, 0, 0)
   red_1 = (186, 6, 27)
   green = (0, 255, 0)
   blue = (0, 0, 255)
   blue_1 = (25, 7, 122)
   purp_0 = (136, 11, 181)
   sleep = (180, 180, 188)
   d_yellow = (242, 201, 15)
   grey_a = (127, 126, 133)

   @staticmethod
   def str_to_color(buff: str):
      if "kill" in buff.lower():
         return sysColors.red_1
      if "trk" in buff.lower():
         return sysColors.d_yellow
      if "rtn" in buff.lower():
         return sysColors.purp_0
      # -- -- -- --
      return sysColors.green
