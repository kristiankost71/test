# import py_dss_interface
# dss = py_dss_interface.DSSDLL(r"C:\Program Files\OpenDSS")
#
# dsscircuit = circuit
# dss_file = r"C:\Users\krist\Desktop\skuska.dss"
#
# dss.text(f"compile [{dss_file}]")
#
# dss.solution_solve()
#
# dss.text("Show voltage LN Nodes")


import win32com.client
from time import process_time

DSSObj = win32com.client.gencache.EnsureDispatch("OpenDSSEngine.DSS")
DSSText = DSSObj.Text
DSSCircuit = DSSObj.ActiveCircuit
DSSSolution = DSSCircuit.Solution
DSSParallel = DSSCircuit.Parallel
DSSBus=DSSCircuit.ActiveBus
DSSCtrlQueue=DSSCircuit.CtrlQueue
DSSObj.Start(0)

DNumActors = 6
print('Simulation started')
DSSText.Command='ClearAll'
DSSText.Command='compile "C:/Program Files/OpenDSS/IEEETestCases/8500-Node/Master.dss"'
DSSText.Command='set maxiterations=1000 maxcontroliter=1000'
DSSText.Command='plot circuit powers'
DSSSolution.Solve                       # Solves Actor 1
tic = process_time()  # Gets the initial time
for i in range(0,1000):
    j = DSSCircuit.Loads.First
    while j > 0:
        DSSCircuit.Loads.kW = 50
        DSSCircuit.Loads.kvar = 20
        j = DSSCircuit.Loads.Next

toc = process_time() # Gets the final time
# Publish results
print('Total time required (s): ')
print(toc-tic)

