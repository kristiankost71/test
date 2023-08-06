# Create DSS object

import win32com.client

from win32com.client import makepy

import sys

sys.argv = ["makepy", "OpenDSSEngine.DSS"]

makepy.main()

DSSObject = win32com.client.Dispatch("OpenDSSEngine.DSS")

# Start OpenDSS engine (0 means normal mode, 1 means minimized mode)
if not DSSObject.Start(0):
    print('Unable to start OpenDSS')
    exit()

DSSText = DSSObject.Text

DSSCircuit = DSSObject.ActiveCircuit

# Compile a model
DSSText.Command = 'compile "C:/Users/krist/Desktop/MODEE/OpenDSS/Hlavne-zadanie-Kost.txt"'
DSSActiveBus = DSSCircuit.ActiveBus
# Sets bus "myBus" as the active Bus
DSSCircuit.SetActiveBus('myBus')

mykVBase = DSSActiveBus.kVBase
print(mykVBase)


