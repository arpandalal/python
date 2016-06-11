import httplib, urllib
import psutil
import time

import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()

def doit():
    temp = format(sensor.read_temperature())
    p = format(sensor.read_pressure())
    a = format(sensor.read_altitude())
    sp = format(sensor.read_sealevel_pressure())
    print('Temp = {0:0.2f} *C',temp)
    print('Pressure = {0:0.2f} Pa',p)
    print('Altitude = {0:0.2f} m',a)
    print('Sealevel Pressure = {0:0.2f} Pa',sp)
    params = urllib.urlencode({'field1': temp, 'field2': p, 'field3': a, 'field4': sp,'key':'29QOQE9MGEOS0YD8'})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()

    print (response.status, response.reason)
    data = response.read()
    conn.close()
 
#sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
    while True:
        doit()
        time.sleep(16) 
