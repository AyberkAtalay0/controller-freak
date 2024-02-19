from os import system

try:
  from requests import post
  import base64 as b64, cv2
  from time import sleep
  import mss
  from mss.tools import to_png
except: 
  system("pip install requests")
  system("pip install base64")
  system("pip install mss")

  from requests import post
  import base64 as b64
  from time import sleep
  import mss
  from mss.tools import to_png as to_bytes

def mainloop(fps):
  while 1:
    print("Loop working...")
    try:
      with mss.mss() as visual:
        image = visual.grab(visual.monitors[1])
        post(url="http://127.0.0.1:8547/stream", json={"pixels": str(image.pixels, "bytes": to_png(im.rgb, im.size))}, verify=False)
        print("Image sent.")
    except Exception as e: print(str(e))
    sleep(1/fps)

if __name__ == "__main__":
  mainloop(fps=24)
