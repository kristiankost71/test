import win32com.client

def main():
    # Create an instance of OpenDSS engine
    dss = win32com.client.Dispatch("OpenDSSEngine.DSS")

    # Start OpenDSS engine
    dss.Start(0)

    # Load the circuit file
    circuit_file = r"C:/Users/krist/Desktop/MODEE/OpenDSS/jednoduche.dss"

    # Access the Text property and set the Command to compile the circuit
    dss.Text.Command = f"compile [{circuit_file}]"

    # Access the ActiveCircuit object
    dss_circuit = dss.ActiveCircuit

    # Step through every load and scale it up
    loads = dss_circuit.Loads
    load_index = loads.First

    while load_index:
        load_name = loads.Name  # Get the name of the current load
        dss_circuit.Loads.Name = load_name  # Set the active load to the current load
        dss_circuit.Loads.kW *= 1.2  # Scale up the power of the active load
        load_index = loads.Next


if __name__ == "__main__":
    main()


import win32com.client

def main():
    # Create an instance of OpenDSS engine
    dss = win32com.client.Dispatch("OpenDSSEngine.DSS")

    # Start OpenDSS engine
    dss.Start(0)

    # Load the circuit file
    circuit_file = r"C:/Users/krist/Desktop/MODEE/OpenDSS/jednoduche.dss"

    # Access the Text property and set the Command to compile and solve the circuit
    dss.Text.Command = f"compile [{circuit_file}]"
    dss.Text.Command = "solve"

    # Access the ActiveCircuit object
    dss_circuit = dss.ActiveCircuit

    # Step through every load and scale it up
    loads = dss_circuit.Loads
    load_index = loads.First

    while load_index:
        load_name = loads.Name  # Get the name of the current load
        dss_circuit.Loads.Name = load_name  # Set the active load to the current load
        dss_circuit.Loads.kW *= 1.2  # Scale up the power of the active load
        load_index = loads.Next

    # Save changes to the circuit (optional)
    dss.Text.Command = "save"



if __name__ == "__main__":
    main()
