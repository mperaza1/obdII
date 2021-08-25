import obd

def main():
    print('Hello World')

    '''ports = obd.scan_serial()      # return list of valid USB or RF ports
    print(ports)                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']
    connection = obd.OBD()
    print(connection.status())

    while(1):
      cmd = obd.commands.RPM
      response = connection.query(cmd)
      print(response.value)'''

    obd.logger.setLevel(obd.logging.DEBUG)

    connection = obd.OBD('\\.\\COM5') # auto-connects to USB or RF port
    #connection = obd.OBD() # auto-connects to USB or RF port
    print("Return from obd.OBD")
    cmd = obd.commands.RPM # select an OBD command (sensor)

    response = connection.query(cmd) # send the command, and parse the response

    print(response.value) # returns unit-bearing values thanks to Pint
    #print(response.value.to("mph")) # user-friendly unit conversions


if (__name__ == "__main__"):
  main()
