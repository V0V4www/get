'''import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]
GPIO.setup(dac,GPIO.OUT)
number=[0,0,0,0,0,0,0,0]
GPIO.output(dac,number)
time.sleep(10)
GPIO.output(dac ,0)
GPIO.cleanup()'''
import matplotlib.pyplot as plt
plt.plot([0,2,5,32,64,127,255],[51.5,77.2,115.6,460,870,1670,3250],marker='o')
plt.show()