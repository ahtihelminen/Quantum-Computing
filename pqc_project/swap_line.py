from cirq import *

class SWAP_Compiled_Line_Circuit:
    def __init__(self, line_ciruit, n_of_qubits):
        self.circuit = line_ciruit
        self.compiled = Circuit()
        self.qubits = LineQubit.range(n_of_qubits)

    def __str__(self) -> str:
        return str(self.compiled)

    def main(self):
        for moment in self.circuit:
            for operation in moment:
                if isinstance(operation.gate, type(CNOT)):
                    control, target = operation.qubits
                    c_x, t_x = control.x, target.x
                    if control.is_adjacent(target):
                        self.compiled.append(CNOT(self.qubits[c_x], self.qubits[t_x]))
                    else:
                        diff = c_x - t_x
                        swap_schedule = []
                        idx = 0
                        while diff<-1:
                            swap_schedule.insert(idx, SWAP(self.qubits[c_x], self.qubits[c_x + 1]))
                            idx += 1
                            swap_schedule.insert(idx, SWAP(self.qubits[c_x + 1], self.qubits[c_x]))
                            c_x += 1
                            diff += 1

                        while diff>1:
                            swap_schedule.append(SWAP(self.qubits[c_x], self.qubits[c_x - 1]))
                            idx += 1
                            swap_schedule.append(SWAP(self.qubits[c_x - 1], self.qubits[c_x]))
                            c_x -= 1
                            diff -= 1

                        swap_schedule.insert(idx, CNOT(self.qubits[c_x], self.qubits[t_x]))

                        for gate in swap_schedule:
                            self.compiled.append(gate)
                else:
                    self.compiled.append(operation)

                        