
import cv2, time
from picamera2 import MappedArray
# -- system --
from sys_core.sysColors import sysColors
from sys_core.targetBox import targetBox


# -- color r, g, b --
col_green = (0, 255, 0)
# -- OSD positions --
top_ln = 30
dts_org = (20, top_ln)
hb_org = (290, top_ln)
ai_mode_org = (406, top_ln)
ai_actv_org = (406, (top_ln * 2))
ai_stat_org = (406, (top_ln * 3))
baro_org = (80, 466)
targ_org_s = (210, 130)
targ_org_e = (430, 350)
# -- -- text & etc -- --
scale: float = 0.72
font = cv2.FONT_HERSHEY_SIMPLEX


class vtxOverlay(object):

   def __init__(self):
      self.ai_mode: str = "OFF"
      self.ai_stat: str = "OFF"
      self.ai_act: str = "OFF"
      self.baro_temp: () = (0.0, 0.0, 0.0)
      self.targ_box_color = sysColors.sleep
      self.draw_thickness = 2
      self.last_rf_hb: str = "X"
      self.trg_box: targetBox = targetBox()

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   def update(self, ai_m = None, ai_a = None, ai_s = None):
      self.ai_mode = ai_m if ai_m is not None else self.ai_mode
      self.ai_stat = ai_s if ai_s is not None else self.ai_stat
      self.ai_act = ai_a if ai_a is not None else self.ai_act

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   def call_on_frame(self, req):
      with MappedArray(req, "main") as m:
         self.__datetime(m)
         self.__rf_hb(m)
         self.__ai_action(m)
         self.__ai_trigger_on(m)
         self.__ai_status(m)
         self.__baro_temp(m)
         # -- target box --
         self.__target_box(m)

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   def __datetime(self, m: MappedArray):
      timestamp = time.strftime("'%y/%m/%d %X")
      cv2.putText(m.array, timestamp, dts_org, font, scale
         , sysColors.green, self.draw_thickness)

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   def __ai_action(self, m: MappedArray):
      x_offset: int = 60
      cv2.putText(m.array, "AI/a:", ai_mode_org, font, scale
         , sysColors.green, self.draw_thickness)
      x, y = ai_mode_org
      txtcolor: () = sysColors.str_to_color(self.ai_mode)
      cv2.putText(m.array, self.ai_mode, ((x + x_offset), y)
         , font, scale, txtcolor, self.draw_thickness)

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   def __ai_status(self, m: MappedArray):
      x_offset: int = 60
      cv2.putText(m.array, "AI/s:", ai_stat_org, font, scale
         , sysColors.green, self.draw_thickness)
      x, y = ai_stat_org
      txtcolor: () = sysColors.str_to_color(self.ai_stat)
      cv2.putText(m.array, self.ai_stat, ((x + x_offset), y)
         , font, scale, txtcolor, self.draw_thickness)

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   def __ai_trigger_on(self, m: MappedArray):
      x_offset: int = 60
      cv2.putText(m.array, "AI/t:", ai_actv_org, font
         , scale, sysColors.green, self.draw_thickness)
      txtcolor: () = sysColors.str_to_color(self.ai_act)
      x, y = ai_actv_org
      cv2.putText(m.array, self.ai_act, ((x + x_offset), y)
         , font, scale, txtcolor, self.draw_thickness)

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   def __baro_temp(self, m: MappedArray):
      alt, h, t = self.baro_temp
      buff: str = f"A: {alt}m P: {h}hPa T: {t}*C"
      cv2.putText(m.array, buff, baro_org, font, scale
         , sysColors.green, self.draw_thickness)

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   def __target_box(self, m: MappedArray):
      cv2.rectangle(m.array, targ_org_s, targ_org_e
         , self.targ_box_color, self.draw_thickness)

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   def __rf_hb(self, m: MappedArray):
      cv2.putText(m.array,"rfHB:", hb_org, font, scale
         , sysColors.green, self.draw_thickness)
      x_offset: int = 60; x, y = hb_org
      sym_color: () = sysColors.blue
      if self.last_rf_hb in ["?", "!"]:
         sym_color = sysColors.d_yellow
      if self.last_rf_hb in ["X", "-"]:
         sym_color = sysColors.red_1
      # -- -- -- --
      cv2.putText(m.array, self.last_rf_hb, (x + x_offset, y)
         , font, scale, sym_color, self.draw_thickness)
