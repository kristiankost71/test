# Create DSS object

import win32com.client

from win32com.client import makepy

import sys

sys.argv = ["makepy", "OpenDSSEngine.DSS"]

makepy.main()

DSSObject = win32com.client.Dispatch("OpenDSSEngine.DSS")

DSSText = DSSObject.Text
DSSCircuit = DSSObject.ActiveCircuit

# Compile a model

DSSText.Command = 'compile "C:/Program Files/OpenDSS/EPRITestCircuits/ckt5/Transformers_ckt5.dss"'

DSSXfmr = DSSCircuit.Transformers



