## Quantum Computing Projects

### 1. Swap Scheduling Algorithm for Line and Grid Circuits
The project was conducted as a final project of Practical Quantum Computing course (CS-C3260) at Aalto University.

Quantum circuit execution is often constrained by the topology of the underlying hardware. This is particularly true for **superconducting qubit** and **neutral atom processors**, which are restricted to adjacent-qubit gate operations. Consequently, executing non-adjacent multi-qubit gate operations requires inserting adjacent **SWAP gates** until the involved qubits are brought into proximity. This series of SWAP gates is called a **SWAP schedule**.

The code contains classes `Random_Circuit_Generator`, `SWAP_Compiled_Line_Circuit` and `SWAP_Compiled_Grid_Circuit` from which the first allows the creation of $n$ qubit line or grid Cirq circuit that gets randomly implemented with `H`, `X` and `CNOT` gates. The last two classes input a generated circuit and compile a SWAP scheduled version of the circuit. Additionally in `tools.py` there's a function `simulate_and_compare` which can be used to compare the results of the SWAP scheduled circuit to the original one and thus validate the scheduling protocol.

### 2. Bernstein-Vazirani Circuit Optimizer
This notebook presents a Cirq circuit implementation of the Bernstein-Vazirani algorithm. Addittionally it presents an optimizatin algorithm that applies four different circuit identities to optimize the original circuit. Finally the optimized circuit is benchmarked against the original circuit and the difference in runtimes is visualized.

### 3. Variational Quantum Eigensolver
This notebook presents a random Hamiltonian generator and both noisy and noiseless VQE methods for the estimation of the generated Hamiltonians ground energy. For the noisless method it uses gradient descent calculted with the parameter shift rule and straightforward algebraic calculation of the energy expectation value. For noisy VQE it uses Qiskit's noisy Aer simulator for the energy expectation value definition and SciPy's minimize function with COBYLA solver to find the ground state energy.

