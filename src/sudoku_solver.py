from qiskit import Aer, QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit.visualization import plot_histogram
from grover_utils import construct_oracle, diffusion_operator
import matplotlib.pyplot as plt

def initialize_sudoku_state(puzzle):
    """Initialize the puzzle with known values."""
    qr = QuantumRegister(4)
    circuit = QuantumCircuit(qr)

    # Initialize known values in the Sudoku grid
    for i, value in enumerate(puzzle):
        if value == 1:
            circuit.x(qr[i])  # Apply X gate to represent '1' in that cell
    return circuit

def solve_sudoku(puzzle):
    """Solves the 2x2 Sudoku puzzle using Grover's algorithm."""
    qr = QuantumRegister(4)
    cr = ClassicalRegister(4)
    circuit = QuantumCircuit(qr, cr)

    # Initialize the puzzle
    init_circuit = initialize_sudoku_state(puzzle)
    circuit.compose(init_circuit, inplace=True)

    # Apply Hadamard gates to create superposition
    circuit.h(qr)

    # Construct and apply the Grover operator (oracle + diffusion)
    oracle = construct_oracle()
    circuit.compose(oracle, inplace=True)
    diffusion = diffusion_operator(len(qr))
    circuit.compose(diffusion, inplace=True)

    # Measurement
    circuit.measure(qr, cr)

    # Execute the circuit
    backend = Aer.get_backend('qasm_simulator')
    result = execute(circuit, backend, shots=1024).result()
    counts = result.get_counts()

    # Plot the results
    plot_histogram(counts)
    plt.show()

    return counts

# Example 2x2 puzzle (0 = unknown, 1 = pre-filled cell with value)
# Example puzzle layout:
# [1, 0, 0, 0]  # Represents a 2x2 puzzle with the first cell filled as '1'
example_puzzle = [1, 0, 0, 0]
solution = solve_sudoku(example_puzzle)
print("Solution counts:", solution)
