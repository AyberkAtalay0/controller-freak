from os import system

try:
  from requests import post
  import base64 as b64, cv2
  from time import sleep
  import mss
  from mss.tools import to_png as to_bytes
except: 
  system("pip install requests")
  system("pip install base64")
  system("pip install opencv-python")
  system("pip install mss")

  from requests import post
  import base64 as b64, cv2
  from time import sleep
  import mss
  from mss.tools import to_png as to_bytes

def mainloop(fps):
  while 1:
    sleep(1/fps)
    try:
      with mss.mss() as visual:
        monitor = visual.monitors[1]
        img = visual.grab(monitor)
        raw_bytes = to_bytes(img.rgb, im.size)
        print("raw_bytes:", str(raw_bytes)[:15])
    except Exception as e: print(str(e))
    print("loop")

if __name__ == "__main__":
  mainloop(fps=12)
