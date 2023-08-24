from dss import DSS as dss_engine


DSSText = dss_engine.Text
DSSCircuit = dss_engine.ActiveCircuit
DSSSolution = dss_engine.ActiveCircuit.Solution
DSSParallel = dss_engine.ActiveCircuit.Parallel
DSSLines = dss_engine.ActiveCircuit.Lines
DSSBus = dss_engine.ActiveCircuit.ActiveBus

dss_engine.Text.Command = 'Clear'
dss_engine.Text.Command = 'New Circuit.Source phases=3 bus1=A basekv=400 R1=0.000000001 X1=0.0000000001'
dss_engine.Text.Command = 'New Line.VED Bus1=A Bus2=B Length=100 Units=km R1=0.03017 X1=0.41469 B1=2.712357'
dss_engine.Text.Command = 'New Load.zataz bus=B kv=400 kw=150000 pf=0.78 model=1 Vmaxpu=2 Vminpu=0.0'

dss_engine.ActiveCircuit.Solution.Solve()
voltages = dss_engine.ActiveCircuit.AllBusVolts

for i in range(len(voltages) // 2):
    print('node %d: %f + j%f' % (i, voltages[2*i], voltages[2*i + 1]))

dss_engine.Text.Command = 'Show Voltage LN Nodes'



