import py_dss_interface
opendss_path = "C:/Program Files/OpenDSS"
dss = py_dss_interface.DSSDLL(opendss_path)
dss_file = r"C:\Users\krist\Desktop\MODEE\OpenDSS\Hlavne-zadanie-Kost.txt"
dss.text("compile {}".format(dss_file))
dss.solution_solve()
dss.text("show voltages")
allbusvolts = dss.circuit_all_bus_volts()
print(dss.circuit_all_bus_volts())
