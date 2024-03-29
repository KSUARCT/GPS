
from rct_sae_gps import UbloxGps
import serial

port = serial.Serial('/dev/serial0', baudrate=38400, timeout=1)
gps = UbloxGps(port)

def run():
  
  try: 
    print("Listenting for UBX Messages.")
    while True:
      try: 
        coords = gps.geo_coords()
        lon = gps.lon
        lat = gps.lat
        print(lon,lat)
      except (ValueError, IOError) as err:
        print(err)
  
  finally:
    port.close()

if __name__ == '__main__':
  run()