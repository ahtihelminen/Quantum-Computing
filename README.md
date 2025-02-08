## Compiling Quantum Circuits for Neutral Atoms Array Processors

### Problem Statement  
Quantum circuit execution is often constrained by the topology of the underlying hardware. This is particularly true for **superconducting qubit** and **neutral atom processors**, which are restricted to adjacent-qubit gate operations. Consequently, executing non-adjacent multi-qubit gate operations requires inserting adjacent **SWAP gates** until the involved qubits are brought into proximity. This series of SWAP gates is called a **SWAP schedule**. The number of possible SWAP schedules increases exponentially with the number of qubits, and excessive consecutive SWAP gates can lead to significant error accumulation. Since finding the schedule with minimal circuit depth is extremely complex, SWAP scheduling as compiling method scales poorly.

A promising solution to this problem involves **Dynamically Field-Programmable Quantum Arrays (DPQA)**, where atomic qubits are loaded into optical traps that can be reconfigured during computation. In this project, our goal is to develop a heuristic for compiling **Cirq** quantum circuits optimized for DPQA by leveraging both **qubit movement** and **SWAP gates**. Additionally, we aim to visualize this compilation process to make it more comprehensible.

### Methods  
We will begin by developing a program that:
1. Generates a quantum circuit with **n > 1 qubits** in Cirq, randomly placing `X`, `H`, and `CNOT` gates.
2. Produces a viable SWAP schedule for the generated circuit.

Next, we will implement a visualization tool for a **2D atom array**, supporting arrays of arbitrary size and capable of displaying two types of traps: **Acousto-Optic Deflectors (AOD)** and **Spatial Light Modulators (SLM)**.

Once this is achieved, we will develop the following heuristics:
1. Moving one row or column of an AOD.
2. Transferring a qubit from an AOD to an SLM.
3. Swapping two qubits between two traps.

Finally, we will expand the visualization program to display atom movements and swaps. We will also develop a general **DPQA compiler** for Cirq circuits.

### Expected Results  
Previous research [1] indicates that circuits compiled for DPQA should result in a significantly lower number of two-qubit gates compared to traditional SWAP schedules. This reduction is crucial for enhancing the scalability and efficiency of the DPQA architecture.

## References

This report mainly used the information and problem formulation stated in [PQC 2024 Project list](https://mycourses.aalto.fi/pluginfile.php/2348133/mod_resource/content/1/Practical%20Quantum%20Computing%202024%20Fall%20Project%20List.pdf) document. Additionally Quantum Zeitgeist [article on DPQA](https://quantumzeitgeist.com/dpqa-a-promising-platform-for-quantum-computing-with-dynamic-qubit-arrays/) was used to understand the topic better.

The referenced paper is:

[1] [Compiling Quantum Circuits for Dynamically Field-Programmable Neutral Atoms Array Processors](https://quantum-journal.org/papers/q-2024-03-14-1281/)
