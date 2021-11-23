import serial
import sys
import time

if __name__=="__main__":
    ser = serial.Serial('/dev/ttyUSB0', 38400)
    bufs = ""
    start = time.monotonic()
    while True:
        ser.write(0x1A)
        bufs = bufs + str(ser.read(1),'utf-8', errors='ignore')
        end = time.monotonic()
        if end - start > 0.5: 
            print(bufs,end="")
            bufs = ""
            start = time.monotonic()
    ser.close()