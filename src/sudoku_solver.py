from qiskit import Aer, QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit.visualization import plot_histogram
from grover_utils import construct_oracle, diffusion_operator
import matplotlib.pyplot as plt

def initialize_sudoku_state(puzzle):
    """Initialize the puzzle with known values.
    
    This function sets up the initial state of the quantum circuit based on
    the provided Sudoku puzzle. The known values are represented as qubits 
    in the quantum circuit.

    Args:
        puzzle (list): A list representing the Sudoku puzzle, where 1 indicates 
                       a pre-filled cell and 0 indicates an unknown cell.

    Returns:
        QuantumCircuit: A quantum circuit initialized with the known values of the puzzle.
    """
    # Create a quantum register for 4 qubits (for a 2x2 Sudoku puzzle)
    qr = QuantumRegister(4)
    circuit = QuantumCircuit(qr)

    # Initialize known values in the Sudoku grid
    for i, value in enumerate(puzzle):
        if value == 1:
            circuit.x(qr[i])  # Apply X gate to represent '1' in that cell
    return circuit

def solve_sudoku(puzzle):
    """Solves the 2x2 Sudoku puzzle using Grover's algorithm.
    
    This function constructs a quantum circuit to solve the provided Sudoku 
    puzzle using Grover's search algorithm. The circuit includes an oracle 
    that encodes the Sudoku constraints and a diffusion operator to amplify 
    the correct solutions.

    Args:
        puzzle (list): A list representing the Sudoku puzzle, where 1 indicates 
                       a pre-filled cell and 0 indicates an unknown cell.

    Returns:
        dict: A dictionary containing the counts of measured states after execution.
    """
    # Create quantum and classical registers
    qr = QuantumRegister(4)  # Quantum register with 4 qubits
    cr = ClassicalRegister(4)  # Classical register for measurement
    circuit = QuantumCircuit(qr, cr)  # Create the quantum circuit

    # Initialize the puzzle
    init_circuit = initialize_sudoku_state(puzzle)  # Get the initialization circuit
    circuit.compose(init_circuit, inplace=True)  # Compose it into the main circuit

    # Step 1: Apply Hadamard gates to create superposition of all states
    circuit.h(qr)

    # Step 2: Construct and apply the Grover operator (oracle + diffusion)
    oracle = construct_oracle()  # Get the oracle that enforces Sudoku constraints
    circuit.compose(oracle, inplace=True)  # Compose the oracle into the circuit
    diffusion = diffusion_operator(len(qr))  # Create the diffusion operator
    circuit.compose(diffusion, inplace=True)  # Compose the diffusion operator into the circuit

    # Step 3: Measurement of the quantum states
    circuit.measure(qr, cr)  # Measure the quantum register into the classical register

    # Step 4: Execute the circuit on a quantum simulator
    backend = Aer.get_backend('qasm_simulator')  # Use the QASM simulator backend
    result = execute(circuit, backend, shots=1024).result()  # Execute and get results
    counts = result.get_counts()  # Get the counts of measurement results

    # Step 5: Plot the results using a histogram
    plot_histogram(counts)  # Plot the measurement results
    plt.show()  # Display the plot

    return counts  # Return the counts of solutions

# Example 2x2 puzzle (0 = unknown, 1 = pre-filled cell with value)
# Example puzzle layout:
# [1, 0, 0, 0]  # Represents a 2x2 puzzle with the first cell filled as '1'
example_puzzle = [1, 0, 0, 0]
solution = solve_sudoku(example_puzzle)  # Solve the Sudoku puzzle
print("Solution counts:", solution)  # Print the solution counts
