import matplotlib.pyplot as plt
from cirq import *

def simulate_and_compare(original_circuit: Circuit, SWAP_circuit: Circuit, repetitions: int = 100000):
    """
    Simulates two Cirq circuits and plots their measurement statistics on the same histogram.

    Args:
        circuit1 (cirq.Circuit): The first Cirq circuit to simulate.
        circuit2 (cirq.Circuit): The second Cirq circuit to simulate.
        repetitions (int): The number of times to simulate each circuit.

    Returns:
        None
    """
    # Create a simulator
    simulator = Simulator()

    n_qubits = len(original_circuit.all_qubits())

    # Simulate the first circuit
    result1 = simulator.run(original_circuit, repetitions=repetitions)
    measurement_keys1 = [str(key) for key in original_circuit.all_measurement_key_objs()]
    if not measurement_keys1:
        raise ValueError("The first circuit has no measurement operations.")
    stats1 = result1.histogram(key=measurement_keys1[0])

    # Simulate the second circuit
    result2 = simulator.run(SWAP_circuit, repetitions=repetitions)
    measurement_keys2 = [str(key) for key in SWAP_circuit.all_measurement_key_objs()]
    if not measurement_keys2:
        raise ValueError("The second circuit has no measurement operations.")
    stats2 = result2.histogram(key=measurement_keys2[0])


    def in_binary(s: int):
        s = bin(s)
        s = s[2:]
        l = len(s)
        s = (n_qubits-l)*'0' + s
        return s


    # Prepare data for plotting
    outcomes1 = list(in_binary(x) for x in stats1.keys())
    frequencies1 = list(stats1.values())
    outcomes2 = list(in_binary(x) for x in stats2.keys())
    frequencies2 = list(stats2.values())

    # Align the bars using offsets
    bar_width = 0.4

    # Plot both histograms
    plt.bar(outcomes1, frequencies1, width=bar_width, align='edge', label='Original circuit', alpha=0.7)
    plt.bar(outcomes2, frequencies2, width=-bar_width, align='edge', label='SWAP scheduled circuit', alpha=0.7)

    plt.xticks(outcomes1, labels=outcomes1, rotation=45, ha="right")

    # Add labels, legend, and grid
    plt.xlabel("Measurement Outcome")
    plt.ylabel("Frequency")
    plt.title("Comparison of Measurement Results")
    plt.xticks(outcomes1)  # Assuming the outcomes are the same for simplicity
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
