from cirq import *
import random

class Random_Circuit_Generator:

    def random_gate(self):
        gates = [H, X, CNOT]
        return random.choice(gates)

    def generate_1D(self, n_of_qubits, iteration_limit=1):
        circuit = Circuit()
        qubits = [LineQubit(i) for i in range(n_of_qubits)]

        for _ in range(iteration_limit):
            for qubit in qubits:
                gate = self.random_gate()
                #print(gate)
                if isinstance(gate, type(CNOT)):
                    control = qubit
                    possible_targets = qubits.copy()
                    possible_targets.remove(qubit)
                    target = random.choice(possible_targets)
                    circuit.append(gate(control, target))
                else:
                    circuit.append(gate(qubit))

        circuit.append(measure(*qubits, key='Result'))

        return circuit

    def generate_2D(self, height, width, iteration_limit=1):
        circuit = Circuit()
        qubits = [[GridQubit(row, col) for col in range(width)] for row in range(height)]
        qubits_flat = [q for r in qubits for q in r]

        for _ in range(iteration_limit):
            for row in range(height):
                for col in range(width):
                    qubit = qubits[row][col]
                    gate = self.random_gate()
                    
                    if gate == CNOT:
                        # Choose a random neighboring qubit as the target for CNOT                        
                        possible_targets = qubits_flat.copy()
                        possible_targets.remove(qubit)

                        if possible_targets:
                            target = random.choice(possible_targets)
                            circuit.append(CNOT(qubit, target))
                    else:
                        circuit.append(gate(qubit))
        
        circuit.append(measure(*qubits_flat, key='result'))
        
        return circuit   
