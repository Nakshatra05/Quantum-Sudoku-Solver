# Quantum Sudoku Solver

## Overview

The **Quantum Sudoku Solver** is an innovative implementation of a Sudoku puzzle solver leveraging quantum computing principles, specifically Grover's algorithm. This project demonstrates how quantum algorithms can be applied to solve constraint satisfaction problems like Sudoku, which require finding valid configurations based on given constraints.

### Features
- Solves 2x2 Sudoku puzzles using Grover's algorithm.
- Provides visualization of solution counts.
- Easy to extend for larger Sudoku puzzles with additional implementations.

## Table of Contents
- [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
- [Theory](#theory)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Background

Sudoku is a popular logic-based puzzle that consists of a grid of cells, each containing numbers. The objective is to fill the grid so that each column, row, and sub-grid contains all digits without repetition. This solver applies Grover's algorithm, which is known for its quadratic speedup in unstructured search problems, to find valid Sudoku solutions.

### Grover's Algorithm

Grover's algorithm allows us to search for a solution among \( N \) possible solutions in \( O(\sqrt{N}) \) time, making it significantly faster than classical approaches that generally require \( O(N) \). In the context of Sudoku, the algorithm helps identify valid arrangements of numbers while adhering to the constraints of the puzzle.

## Installation

To get started with the Quantum Sudoku Solver, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Quantum-Sudoku-Solver.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Quantum-Sudoku-Solver
   ```

3. **Install Required Packages**:
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

   This will install the necessary libraries including Qiskit for quantum computing functionalities and Matplotlib for visualizations.

## Usage

To run the Sudoku solver, execute the following command in your terminal:

```bash
python src/sudoku_solver.py
```

### Example Puzzle
In the `sudoku_solver.py` file, you can modify the example puzzle:
```python
example_puzzle = [1, 0, 0, 0]  # Represents a 2x2 Sudoku grid
```
- `1` indicates a filled cell.
- `0` indicates an empty cell that needs to be solved.

## Theory

### Quantum Computing and Sudoku

Quantum computing leverages the principles of quantum mechanics to process information. In this project, we utilize the following concepts:

1. **Superposition**: Quantum bits (qubits) can exist in multiple states simultaneously, allowing the algorithm to explore multiple potential solutions at once.

2. **Entanglement**: Qubits can be interconnected, meaning the state of one qubit can depend on the state of another, enabling complex relationships that are essential for enforcing Sudoku rules.

3. **Quantum Oracle**: This is a crucial component of Grover's algorithm. The oracle is a black-box function that can recognize valid solutions. In our Sudoku solver, the oracle checks whether a set of qubit states violates Sudoku rules.

4. **Amplitude Amplification**: Grover's algorithm iteratively amplifies the probability of correct states while diminishing the amplitude of incorrect states, guiding the measurement toward valid solutions.

### Constructing the Oracle

In our implementation, we construct a quantum oracle for a simple 2x2 Sudoku puzzle:
- It enforces constraints that specific qubit states must differ from one another to comply with Sudoku rules.

### Visualization

The results of the solver are visualized using a histogram that displays the counts of potential solutions, providing insights into the configurations explored by the algorithm.

## Project Structure

The project is organized as follows:

```
Quantum-Sudoku-Solver/
├── README.md               # Project documentation
├── LICENSE                 # License information
├── src/                    # Source code directory
│   ├── sudoku_solver.py    # Main Sudoku solver script
│   └── grover_utils.py     # Utilities for Grover's algorithm
├── requirements.txt        # Python package dependencies
```

### Key Files

- **sudoku_solver.py**: Contains the main logic for solving the Sudoku puzzle.
- **grover_utils.py**: Includes functions for constructing the oracle and the diffusion operator.
- **requirements.txt**: Lists all required packages for running the project.

## Contributing

Contributions to the Quantum Sudoku Solver are welcome! If you'd like to contribute, please follow these steps:

1. **Fork the Repository**: Click on the “Fork” button at the top right of this page.
2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/your-username/Quantum-Sudoku-Solver.git
   ```
3. **Create a New Branch**:
   ```bash
   git checkout -b feature/YourFeature
   ```
4. **Make Your Changes**: Implement new features or fix issues.
5. **Commit Your Changes**:
   ```bash
   git commit -m "Add your message here"
   ```
6. **Push to Your Fork**:
   ```bash
   git push origin feature/YourFeature
   ```
7. **Create a Pull Request**: Submit your changes for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for your interest in the Quantum Sudoku Solver! We hope you find it useful for exploring quantum computing and constraint satisfaction problems.
