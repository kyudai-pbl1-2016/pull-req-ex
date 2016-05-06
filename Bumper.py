from create2.create2 import Create2
import time

def get_bumper(create2):
     if create2.get_sensor().bumpsWheeldrops == 0:
          return 0
     else:
          return 1

#ˆÈ‰ºƒeƒXƒg
create = Create2(threading=True)

while 1:
    print get_bumper(create)
    time.sleep(1.0)