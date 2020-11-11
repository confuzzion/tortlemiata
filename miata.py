import obd

connection = obd.OBD("/dev/rfcomm0") # auto-connects to USB or RF port

while(True): #prints RPM over and over again
  #cmd = obd.commands.RPM
  #response = connection.query(cmd)
  #print(response.value)
  print(connection.query(obd.commands.RPM).value)
