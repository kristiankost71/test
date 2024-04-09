from dss import DSS as dss_engine
import cmath
import matplotlib.pyplot as plt

DSSText = dss_engine.Text
DSSCircuit = dss_engine.ActiveCircuit
DSSSolution = dss_engine.ActiveCircuit.Solution
DSSParallel = dss_engine.ActiveCircuit.Parallel
DSSLines = DSSCircuit.Lines
DSSActiveBus = DSSCircuit.ActiveBus
DSSActiveElement = DSSCircuit.ActiveCktElement

VoltageIN = []
VoltageOUT = []
VoltageRES = []
Subeh1 = []
# Výpočet kapacitne indukovaného napätia
# for i in range(1,5):
#      dss_engine.Text.Command = 'Clear'
#      dss_engine.Text.Command = 'Set DefaultBaseFrequency=50'
#      dss_engine.Text.Command = 'New Circuit.Source phases=3 bus1=A basekv=400 R1=0.000000001 X1=0.0000000001'
#      dss_engine.Text.Command = 'New Wiredata.silov Rac=0.646847 Runits=km GMRac=0.13589  GMRUnits=cm Radius=0.50546 Radunits=cm'
#      dss_engine.Text.Command = 'New Wiredata.AJ_HHAH_12x2x1 Rac=1.846 Runits=km  Radius=16.1   Radunits=mm'
#      dss_engine.Text.Command = 'New CNData.TCEKEZE_12x2_1.2 Normamps=6 Runits=m Rac=0.0159 Rstrand=0.056 GMRUnits=mm Radunits=mm radius=0.6  InsLayer=0.6 DiaStrand=0.47 DiaCable=34.8 EpsR = 2.3 k=16'
# #    nahodny kabel TS
# #    dss_engine.Text.Command = 'New TSData.TS_1/0 NormAmps=165 DIAM=0.368 GMRac=0.13320 Rac=0.97 Runits=mi Radunits=in gmrunits=in EpsR=2.3 Ins=0.220 DiaIns=0.82 DiaCable=1.06 DiaShield=0.88 TapeLayer=0.005 TapeLap=20'
#      dss_engine.Text.Command = 'New Linegeometry.silove_vedenie nconds=4 cond=1 Wire=silov x=0 h=10 units=m cond=2 Wire=silov x=2 h=10 units=m '
#      dss_engine.Text.Command = 'cond=3 Wire=silov x=1 h=10 units=m cond=4 cncable=TCEKEZE_12x2_1.2 x=3 h=6 units=m '
#      dss_engine.Text.Command = 'New Line.VED Bus1=A.1.2.3.4 Bus2=B.1.2.3.4 Geometry = silove_vedenie Length='+str(i)+' Units=km'
#      dss_engine.Text.Command = 'New Load.zataz bus=B.1.2.3.4  kv=400 kw=150000 pf=0.78 model=1 Vmaxpu=2 Vminpu=0.0'
#      dss_engine.ActiveCircuit.Solution.Solve()
#      DSSCircuit.SetActiveBus('A')
#      myVolt = DSSActiveBus.VMagAngle
#      VoltageIN.append(round((myVolt[6]),3))
#      Subeh1.append(i)
#      DSSCircuit.SetActiveBus('B')
#      myVolt = DSSActiveBus.VMagAngle
#      VoltageOUT.append(round((myVolt[6]),3))
#      VoltageRES.append(VoltageIN[i-1] - VoltageOUT[i-1])

# dss_engine.Text.Command = 'Show Voltage LN Nodes'
#
# plt.plot(Subeh1,VoltageRES,label="Indukované napätie")
# plt.ylabel('U(V)')
# plt.xlabel('l(km)')
# plt.title('Zmena indukovaneho napätia zmenou dĺžky')
# plt.show()



import cmath
import matplotlib.pyplot as plt



# Výpočet kapacitne indukovaného napätia
# for i in range(1,5):
#      dss_engine.Text.Command = 'Clear'
#      dss_engine.Text.Command = 'Set DefaultBaseFrequency=50'
#      dss_engine.Text.Command = 'New Circuit.Source phases=3 bus1=A basekv=400 R1=0.000000001 X1=0.0000000001'
#      dss_engine.Text.Command = 'New Wiredata.silov Rac=0.646847 Runits=km GMRac=0.13589  GMRUnits=cm Radius=0.50546 Radunits=cm'
#      dss_engine.Text.Command = 'New Wiredata.AJ_HHAH_12x2x1 Rac=1.846 Runits=km  Radius=16.1   Radunits=mm'
#      dss_engine.Text.Command = 'New CNData.TCEKEZE_12x2_1.2 Normamps=6 Runits=m Rac=0.0159 Rstrand=0.056 GMRUnits=mm Radunits=mm radius=0.6  InsLayer=0.6 DiaStrand=0.47 DiaCable=34.8 EpsR = 2.3 k=16'
# #    nahodny kabel TS
# #    dss_engine.Text.Command = 'New TSData.TS_1/0 NormAmps=165 DIAM=0.368 GMRac=0.13320 Rac=0.97 Runits=mi Radunits=in gmrunits=in EpsR=2.3 Ins=0.220 DiaIns=0.82 DiaCable=1.06 DiaShield=0.88 TapeLayer=0.005 TapeLap=20'
#      dss_engine.Text.Command = 'New Linegeometry.silove_vedenie nconds=4 cond=1 Wire=silov x=0 h=10 units=m cond=2 Wire=silov x=2 h=10 units=m '
#      dss_engine.Text.Command = 'cond=3 Wire=silov x=1 h=10 units=m cond=4 cncable=TCEKEZE_12x2_1.2 x=3 h=6 units=m '
#      dss_engine.Text.Command = 'New Line.VED Bus1=A.1.2.3.4 Bus2=B.1.2.3.4 Geometry = silove_vedenie Length='+str(i)+' Units=km'
#      dss_engine.Text.Command = 'New Load.zataz bus=B.1.2.3.4  kv=400 kw=150000 pf=0.78 model=1 Vmaxpu=2 Vminpu=0.0'
#      dss_engine.ActiveCircuit.Solution.Solve()
#      DSSCircuit.SetActiveBus('A')
#      myVolt = DSSActiveBus.VMagAngle
#      VoltageIN.append(round((myVolt[6]),3))
#      Subeh1.append(i)
#      DSSCircuit.SetActiveBus('B')
#      myVolt = DSSActiveBus.VMagAngle
#      VoltageOUT.append(round((myVolt[6]),3))
#      VoltageRES.append(VoltageIN[i-1] - VoltageOUT[i-1])
#
# dss_engine.Text.Command = 'Show Voltage LN Nodes'
#
# plt.plot(Subeh1,VoltageRES,label="Indukované napätie")
# plt.ylabel('U(V)')
# plt.xlabel('l(km)')
# plt.title('Zmena indukovaneho napätia zmenou dĺžky')
# plt.show()



# Výpočet kapacitne indukovaného prúdu
CurrentIN = []
Subeh2 = []
for i in range(1,5):
     dss_engine.Text.Command = 'Clear'
     dss_engine.Text.Command = 'Set DefaultBaseFrequency=50'
     dss_engine.Text.Command = 'New Circuit.Source phases=3 bus1=A basekv=400 R1=0.000000001 X1=0.0000000001'
#     dss_engine.Text.Command = 'New Wiredata.silov Rac=0.646847 Runits=km GMRac=0.13589  GMRUnits=cm Radius=0.50546 Radunits=cm'
     dss_engine.Text.Command = 'New Wiredata.silov GMR=0.255 DIAM=0.741 RAC=0.0306 Runits=km radunits=m gmrunits=m '
#     dss_engine.Text.Command = 'New Wiredata.AJ_HHAH_12x2x1 Rac=1.846 Runits=km  Radius=16.1   Radunits=mm'
     dss_engine.Text.Command = 'New Wiredata.verifik1   DIAM=0.75  RAC=0.03  Runits=km  radunits=cm'
     dss_engine.Text.Command = 'New Wiredata.verifik2   DIAM=0.5  RAC=0.04  Runits=km  radunits=cm'
#    nahodny kabel TS
#    dss_engine.Text.Command = 'New TSData.TS_1/0 NormAmps=165 DIAM=0.368 GMRac=0.13320 Rac=0.97 Runits=mi Radunits=in gmrunits=in EpsR=2.3 Ins=0.220 DiaIns=0.82 DiaCable=1.06 DiaShield=0.88 TapeLayer=0.005 TapeLap=20'

#    verifikacia
     dss_engine.Text.Command = 'New CNData.verifik  GMRac =0.3 DiaCable=0.75 Rac=0.03 Runits=km GMRUnits=m Radunits=mm Rstrand=0.04 DiaStrand=0.5 k=2'

     dss_engine.Text.Command = 'New Linegeometry.silove_vedenie nconds=6 reduce=yes nphases= 4 cond=1 Wire=silov x=0   h=10 units=m  cond=2 Wire=silov x=2   h=10 units=m  cond=3 Wire=silov x=1   h=10 units=m cond=4 Wire=verifik1    x= 8 h=2 units=m cond=5 Wire=verifik2    x= 7.993 h=2 units=m cond=6 Wire=verifik2    x= 8.007 h=2 units=m '
     dss_engine.Text.Command = 'New Line.VED Bus1=A.1.2.3.4.5.6 Bus2=B.1.2.3.4.5.6  Geometry = silove_vedenie Length=100 Units=km EarthModel=Carson'
     dss_engine.Text.Command = 'New Load.zataz bus=B.1.2.3.4  kv=400 kw=150e3 pf=1 model=1 Vmaxpu=2 Vminpu=0.0'
#     dss_engine.Text.Command = 'New Reactor.RA phases=1 Bus1=A.4 R=0.1 X=0'
#     dss_engine.Text.Command = 'New Reactor.RB phases=1 Bus1=B.4 R=0.1 X=0'

     dss_engine.Text.Command = 'New Reactor.R15 phases=1 Bus1=A.5 R=0.1 X=0'
     dss_engine.Text.Command = 'New Reactor.R25 phases=1 Bus1=B.5 R=0.1 X=0'

     dss_engine.Text.Command = 'New Reactor.R16 phases=1 Bus1=A.6 R=0.1 X=0'
     dss_engine.Text.Command = 'New Reactor.R26 phases=1 Bus1=B.6 R=0.1 X=0'
     dss_engine.ActiveCircuit.Solution.Solve()
     DSSCircuit.SetActiveElement('"Line.VED"')
     myCurr = DSSActiveElement.CurrentsMagAng
     CurrentIN.append(round(myCurr[2],3))
     Subeh2.append(i)
# for item in CurrentIN:
#   print(item)

dss_engine.Text.Command = 'Show Voltage LN Nodes'
dss_engine.Text.Command = 'Show current Elem'
dss_engine.Text.Command = 'Show lineconstants freq=50 units=km'

plt.plot(Subeh2,CurrentIN,label="Indukovaný prúd")
plt.ylabel('I(A)')
plt.xlabel('l(km)')
plt.title('Zmena indukovaneho prúdu zmenou dĺžky')
plt.show()

# mySize = len(myCurr)
# print(mySize)
# VoltageIN3 = []
# for i in range(0,mySize):
#      VoltageIN3.append(round((myCurr[i]),3))
# for item in VoltageIN3:
#      print(item)
