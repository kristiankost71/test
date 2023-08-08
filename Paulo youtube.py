import py_dss_interface

dss = py_dss_interface.DSSDLL(r"C:\Program Files\OpenDSS")

dss_file = r"C:\Users\krist\Desktop\MODEE\OpenDSS\Hlavne-zadanie-Kost.txt"

dss.text(f"compile [{dss_file}]")

#dss.text("Solve")
dss.solution_solve()
dss.text("Show voltages LN node")
