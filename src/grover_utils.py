from qiskit import QuantumCircuit

def construct_oracle():
    """Constructs a simple oracle for a 2x2 Sudoku puzzle.
    
    The oracle is a quantum circuit that enforces certain constraints 
    for solving the Sudoku puzzle. For a 2x2 Sudoku, we ensure that:
    - Qubit 0 and Qubit 1 must represent different values.
    - Qubit 2 and Qubit 3 must also represent different values.
    
    The oracle is constructed using controlled-Z (CZ) gates, which will flip 
    the phase of the state if both qubits involved are in the |1⟩ state. 
    This enforces the condition that the values represented by these qubits 
    cannot be the same.

    Returns:
        QuantumCircuit: A quantum circuit representing the oracle.
    """
    # Create a quantum circuit with 4 qubits for the 2x2 Sudoku puzzle
    oracle = QuantumCircuit(4)

    # Enforcing qubit pairs to be different values
    oracle.cz(0, 1)  # Enforce that qubits 0 and 1 are different
    oracle.cz(2, 3)  # Enforce that qubits 2 and 3 are different
    
    return oracle

def diffusion_operator(num_qubits):
    """Creates the diffusion operator used in Grover's algorithm.
    
    The diffusion operator is responsible for amplifying the probability 
    of measuring valid solutions. It works by reflecting the state around 
    the average amplitude, which increases the chances of measuring the 
    correct solutions in the final step of Grover's algorithm.

    The steps involved in creating the diffusion operator are:
    1. Apply Hadamard gates to all qubits, putting them into a superposition.
    2. Apply X gates to all qubits, which inverts the states.
    3. Apply a Hadamard gate to the last qubit.
    4. Use a multi-controlled NOT (MCX) gate to create the reflection.
    5. Apply a Hadamard gate to the last qubit again.
    6. Apply X gates again to all qubits.
    7. Apply Hadamard gates to all qubits to complete the diffusion process.

    Args:
        num_qubits (int): The number of qubits in the circuit.

    Returns:
        QuantumCircuit: A quantum circuit representing the diffusion operator.
    """
    # Create a quantum circuit with the specified number of qubits
    diffusion = QuantumCircuit(num_qubits)

    # Step 1: Apply Hadamard gates to all qubits to create superposition
    diffusion.h(range(num_qubits))
    
    # Step 2: Apply X gates to all qubits to invert their states
    diffusion.x(range(num_qubits))
    
    # Step 3: Apply Hadamard to the last qubit
    diffusion.h(num_qubits - 1)

    # Step 4: Apply multi-controlled NOT gate for reflection
    diffusion.mcx(list(range(num_qubits - 1)), num_qubits - 1)

    # Step 5: Apply Hadamard to the last qubit again
    diffusion.h(num_qubits - 1)
    
    # Step 6: Apply X gates again to all qubits
    diffusion.x(range(num_qubits))
    
    # Step 7: Apply Hadamard gates to all qubits again to complete diffusion
    diffusion.h(range(num_qubits))
    
    return diffusion
