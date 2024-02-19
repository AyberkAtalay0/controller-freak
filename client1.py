print("Client established.")

from os import system

try:
  from requests import post
  from time import sleep
  from mss import mss
  from mss.tools import to_png
  from uuid import getnode
except: 
  system("pip install requests")
  system("pip install mss")
  system("pip install uuid")

  from requests import post
  from time import sleep
  from mss import mss
  from mss.tools import to_png as to_bytes
  from uuid import getnode

def mainloop(fps):
  while 1:
    print("Loop working...")
    try:
      with mss() as visual:
        image = visual.grab(visual.monitors[1])
        name = hex(getnode())
        post(url="http://127.0.0.1:5000/stream", json={"pixels": str(image.pixels), "name": str(name)}, verify=False)
        print("Image sent to:", str(name))
    except Exception as e: print(str(e))
    sleep(1/fps)

if __name__ == "__main__":
  mainloop(fps=24)
