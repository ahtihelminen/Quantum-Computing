from cirq import *

class SWAP_Compiled_Grid_Circuit:
    def __init__(self, grid_ciruit, rows, cols):
        self.circuit = grid_ciruit
        self.compiled = Circuit()
        self.qubits = [[GridQubit(r, c) for c in range(cols)] for r in range(rows)]
        self.available_qubits = self.qubits.copy()

    def __str__(self) -> str:
        return str(self.compiled)

    def main(self):
        for moment in self.circuit:
            for operation in moment:
                if isinstance(operation.gate, type(CNOT)):
                    control, target = operation.qubits
                    c_row, c_col = control.row, control.col
                    t_row, t_col = target.row, target.col

                    if control.is_adjacent(target):
                        self.compiled.append(CNOT(self.qubits[c_row][c_col], self.qubits[t_row][t_col]))
                    else:
                        diff_x, diff_y = c_col - t_col, c_row - t_row
                        swap_schedule = []
                        idx = 0
                        while diff_x<-1:
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row][c_col], self.qubits[c_row][c_col + 1]))
                            idx += 1
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row][c_col + 1], self.qubits[c_row][c_col]))
                            c_col += 1
                            diff_x += 1

                        while diff_x>1:
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row][c_col], self.qubits[c_row][c_col-1]))
                            idx += 1
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row][c_col-1], self.qubits[c_row][c_col]))
                            c_col -= 1
                            diff_x -= 1

                        while diff_y<-1:
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row][c_col], self.qubits[c_row + 1][c_col]))
                            idx += 1
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row + 1][c_col], self.qubits[c_row][c_col]))
                            c_row += 1
                            diff_y += 1

                        while diff_y>1:
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row][c_col], self.qubits[c_row - 1][c_col]))
                            idx += 1
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row - 1][c_col], self.qubits[c_row][c_col]))
                            c_row -= 1
                            diff_y -= 1

                        if diff_x<0 and diff_y != 0:
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row][c_col], self.qubits[c_row][c_col + 1]))
                            idx += 1
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row][c_col + 1], self.qubits[c_row][c_col]))
                            c_col += 1
                            diff_x += 1
                        
                        elif diff_x>0 and diff_y != 0:
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row][c_col], self.qubits[c_row][c_col-1]))
                            idx += 1
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row][c_col-1], self.qubits[c_row][c_col]))
                            c_col -= 1
                            diff_x -= 1
                            
                        '''
                        elif diff_y<0:
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row][c_col], self.qubits[c_row + 1][c_col]))
                            idx += 1
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row + 1][c_col], self.qubits[c_row][c_col]))
                            c_row += 1
                            diff_y += 1

                        elif diff_y>0:
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row][c_col], self.qubits[c_row - 1][c_col]))
                            idx += 1
                            swap_schedule.insert(idx, SWAP(self.qubits[c_row - 1][c_col], self.qubits[c_row][c_col]))
                            c_row -= 1
                            diff_y -= 1
                        '''
                        swap_schedule.insert(idx, CNOT(self.qubits[c_row][c_col], self.qubits[t_row][t_col]))

                        for gate in swap_schedule:
                            self.compiled.append(gate)
                else:
                    self.compiled.append(operation)

                        