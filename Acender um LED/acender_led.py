from machine  import Pin
import time  

led1 = Pin(3, Pin.OUT)
led2 = Pin(4, Pin.OUT)
botao = Pin(5, Pin.IN, Pin.PULL_UP)
ligado = False

while True:
 

 if botao.value()==0:
    ligado = not ligado
    time.sleep(0.5)
    while botao.value()==0:
      time.sleep(0.01)

 if ligado:

    led1.value(1)
    time.sleep(2)
    led1.value(0)
    time.sleep(2)

    if not ligado: continue

    led2.value(1)
    time.sleep(1)
    led2.value(0)
    time.sleep(1)
 else:
  led1.value(0)
  led2.value(0)