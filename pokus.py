import win32com.client
try:
    DSSObj = win32com.client.Dispatch("OpenDSSEngine.DSS")
except:
    print('Unable to start the OpenDSS Engine')
    raise SystemExit

DSSText = DSSObj.Text
DSSCircuit = DSSObj.ActiveCircuit
DSSLines = DSSCircuit.Lines
print('vsetko okej')
DSSSolution = DSSCircuit.Solution

