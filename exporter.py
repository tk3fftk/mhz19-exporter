from prometheus_client import start_http_server, Gauge
import random
import time
import serial
import mh_z19

CO2 = Gauge('co2_concentration', 'CO2 concentration (ppm)')
INTERVAL = 5


def obtain_co2():
    try:
        val = mh_z19.read()
    except serial.SerialException as e:
        print("error", e)
    else:
        if val:
            CO2.set(val['co2'])


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        obtain_co2()
        time.sleep(INTERVAL)
