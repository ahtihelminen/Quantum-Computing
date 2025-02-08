from rcg import Random_Circuit_Generator
from cirq import *
from gui import GUI
from swap_line import SWAP_Compiled_Line_Circuit
from swap_grid import SWAP_Compiled_Grid_Circuit
import matplotlib.pyplot as plt
import tools



generator = Random_Circuit_Generator()
line_circuit = generator.generate_1D(5, 3)
print(line_circuit)

swap_line_circ = SWAP_Compiled_Line_Circuit(line_circuit, len(line_circuit.all_qubits()))
swap_line_circ.main()
print(swap_line_circ)
#tools.simulate_and_compare(line_circuit, swap_line_circ.compiled)

rows, cols = 3,3
grid_circuit = generator.generate_2D(rows, cols, 5)

swap_grid_circ = SWAP_Compiled_Grid_Circuit(grid_circuit, rows, cols)
swap_grid_circ.main()

tools.simulate_and_compare(grid_circuit, swap_grid_circ.compiled)


g2 = GUI(rows, cols, len(swap_grid_circ.compiled), swap_grid_circ.compiled)
g2.run()
