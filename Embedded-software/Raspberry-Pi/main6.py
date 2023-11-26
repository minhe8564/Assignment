import spidev
import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.output(buzzer, GPIO.LOW)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def analogRead(ch):
    buf = [(1<<2)|(1<<1)|(ch&4)>>2,(ch&3)<<6,0]
    buf = spi.xfer(buf)
    adcValue = ((buf[1]&0xF)<<8)|buf[2]
    return adcValue

try:
    while 1:
        gasValue = analogRead(0)
        print(gasValue)
        
        if gasValue >= 2700:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(0.5)
            
        else:
            GPIO.output(buzzer, GPIO.LOW)
            
        time.sleep(0.2)
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
spi.close()
