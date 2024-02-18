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
        img = visual.grab(visual.monitors[1])
        raw_bytes = to_bytes(img.rgb, img.size)
        post("127.0.0.1", json={"bytes": raw_bytes})
    except Exception as e: print(str(e))

if __name__ == "__main__":
  mainloop(fps=12)
