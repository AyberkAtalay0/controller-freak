print("Client established.")

from os import system

try:
  from requests import post
  from time import sleep
  from mss import mss
  from mss.tools import to_png
  from uuid import getnode
  from PIL import Image
except: 
  system("pip install requests")
  system("pip install mss")
  system("pip install uuid")
  system("pip install pillow")

  from requests import post
  from time import sleep
  from mss import mss
  from mss.tools import to_png as to_bytes
  from uuid import getnode
  from PIL import Image
  
def mainloop(fps):
  while 1:
    print("Loop working...")
    try:
      with mss() as visual:
        image = visual.grab(visual.monitors[1])
        image = Image.frombytes("RGB", image.size, image.rgb)
        image = image.resize((1366, 768))
        name = hex(getnode()) # www.oatis.xyz
        post(url="http://127.0.0.1/stream", json={"pixels": str(list(image.getdata())), "name": str(name)}, verify=False)
        print("Image sent from:", str(name))
    except Exception as e: print(str(e))
    sleep(1/fps)

if __name__ == "__main__":
  mainloop(fps=24)
