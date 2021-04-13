import obd

def main():
  print('Hello World')

  ports = obd.scan_serial()      # return list of valid USB or RF ports
  print(ports)                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']
  connection = obd.OBD()
  print(connection.status())

  cmd = obd.commands.RPM

  response = connection.query(cmd)

  print(response.value)

if (__name__ == "__main__"):
  main()
