from qiskit import QuantumCircuit

def construct_oracle():
    """Constructs a simple oracle for a 2x2 Sudoku puzzle."""
    oracle = QuantumCircuit(4)

    # Example constraints for a 2x2 Sudoku puzzle:
    # Let's assume we want:
    # - Qubit 0 and Qubit 1 to be different (representing two different cells with different values)
    # - Qubit 2 and Qubit 3 to be different (another pair of cells with different values)

    # Enforcing qubit pairs to be different values using controlled-Z gates
    oracle.cz(0, 1)
    oracle.cz(2, 3)
    
    return oracle

def diffusion_operator(num_qubits):
    """Creates the diffusion operator used in Grover's algorithm."""
    diffusion = QuantumCircuit(num_qubits)
    diffusion.h(range(num_qubits))
    diffusion.x(range(num_qubits))
    diffusion.h(num_qubits - 1)
    diffusion.mcx(list(range(num_qubits - 1)), num_qubits - 1)
    diffusion.h(num_qubits - 1)
    diffusion.x(range(num_qubits))
    diffusion.h(range(num_qubits))
    return diffusion
