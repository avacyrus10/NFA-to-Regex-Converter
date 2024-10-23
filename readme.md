# NFA to Regular Expression Converter

This project implements an algorithm that converts a **Non-deterministic Finite Automaton (NFA)** to a **Regular Expression (regex)**. The algorithm eliminates states from the NFA, ultimately producing a single transition that represents the regular expression for the language recognized by the NFA.

## Features

- **NFA Input:** The program allows for inputting an NFA through the command line, including states, transitions, and final states.
- **State Elimination:** The algorithm eliminates states iteratively, modifying transitions between states to eventually derive the regular expression.
- **Transition Merging:** Multiple transitions between two states are merged using union (OR) operations in the regular expression.
- **Epsilon Transitions:** Epsilon (empty) transitions are used when adding a new final state.
- **Regex Output:** The final result is a regular expression that represents the language accepted by the original NFA.

## Installation

Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nfa-to-regex.git
   cd nfa-to-regex
  ```

## Usage

Run the script using Python:

```bash
python nfa_to_regex.py
```

Input Format: The program expects the following input from the user, entered one after the other:
- Number of states: Enter the total number of states in the NFA.
- Number of transitions: Enter the number of transitions in the NFA.
- Transitions: For each transition, enter three values:
  - i: The source state of the transition (integer).
  - a: The label on the transition (a character or '0' for epsilon).
  - j: The target state of the transition (integer).
- Number of terminal states: Enter the number of terminal (final) states.
- List of terminal states: Enter the terminal states, separated by spaces.

Output: The program will output the regular expression corresponding to the language recognized by the NFA.

## Example

Here’s a sample input and expected output:
Input:

```plaintext

3          # Number of states
3          # Number of transitions
0 a 1      # Transition from state 0 to 1 with 'a'
1 b 2      # Transition from state 1 to 2 with 'b'
2 0 1      # Transition from state 2 to 0 with epsilon (represented by '0')
1          # Number of terminal states
2          # List of terminal states
```
Output:

```plaintext

(a(b)*)    # The regular expression corresponding to the NFA
```