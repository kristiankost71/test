from dss import DSS as dss_engine

DSSText = dss_engine.Text
DSSCircuit = dss_engine.ActiveCircuit
DSSSolution = dss_engine.ActiveCircuit.Solution
DSSParallel = dss_engine.ActiveCircuit.Parallel
DSSLines = dss_engine.ActiveCircuit.Lines
DSSBus = dss_engine.ActiveCircuit.ActiveBus

dss_engine.Text.Command = 'Clear'
dss_engine.Text.Command = 'Set DefaultBaseFrequency=50'
dss_engine.Text.Command = 'New Circuit.Source phases=3 bus1=A basekv=400 R1=0.000000001 X1=0.0000000001'
dss_engine.Text.Command = 'New Wiredata.silov GMR=0.255 DIAM=0.741 RAC=0.0306 Runits=km radunits=m gmrunits=m'
dss_engine.Text.Command = 'New Wiredata.telekom GMR=0.0446 DIAM=0.398 RAC=0.12 Runits=km radunits=m gmrunits=m'
dss_engine.Text.Command = 'New Linegeometry.silove_vedenie nconds=4 nphases=3 cond=1 Wire=silov x=0 h=10 units=m cond=2 Wire=silov x=2 h=10 units=m cond=3 Wire=silov x=1 h=10 units=m cond=4 Wire=telekom x=3 h=18 units=m'
dss_engine.Text.Command = 'New Line.VED Bus1=A.1.2.3.4 Bus2=B.1.2.3.4 Geometry = silove_vedenie Length=100 Units=km'


dss_engine.Text.Command = 'New Reactor.RA phases=1 Bus1=A.4 R=0.1 X=0'
dss_engine.Text.Command = 'New Reactor.RB phases=1 Bus1=B.4 R=0.1 X=0'

dss_engine.Text.Command = 'New Load.zataz bus=B.1.2.3  kv=400 kw=150000 pf=0.78 model=1 Vmaxpu=2 Vminpu=0.0'
dss_engine.ActiveCircuit.Solution.Solve()

dss_engine.Text.Command = 'Show Voltage LN Nodes'
dss_engine.Text.Command = 'Show current'
dss_engine.Text.Command = 'Show lineconstants freq=50 units=km '





