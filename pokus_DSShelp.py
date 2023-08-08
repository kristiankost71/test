import win32com.client
import cmath

from win32com.client import makepy

import sys

sys.argv = ["makepy", "OpenDSSEngine.DSS"]

makepy.main()

# Create DSS object
DSSObject = win32com.client.Dispatch("OpenDSSEngine.DSS")

# Start OpenDSS engine (0 means normal mode, 1 means minimized mode)
if not DSSObject.Start(0):
    print('Unable to start OpenDSS')
    exit()

DSSText = DSSObject.Text
DSSCircuit = DSSObject.ActiveCircuit

# Compile a model
DSSText.Command = 'compile "C:/Program Files/OpenDSS/IEEETestCases/13Bus/IEEE13Nodeckt.dss"'

# Sets bus "myBus" as the active Bus
DSSCircuit.SetActiveBus('myBus')

# Access the ActiveBus property
DSSActiveBus = DSSCircuit.ActiveBus

# Get the puVoltages of the active bus
mypuVolt = DSSActiveBus.puVoltages

myVMagAng = []

# Converts from complex to polar
for i in range(0, len(mypuVolt), 2):
    # Check if the voltage tuple contains both magnitude and angle components
    if i + 1 < len(mypuVolt):
        complex_voltage = complex(mypuVolt[i], mypuVolt[i + 1])
        mag, angle = abs(complex_voltage), cmath.phase(complex_voltage) * 180 / cmath.pi
        myVMagAng.append([mag, angle])

print(myVMagAng)
