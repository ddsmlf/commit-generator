# Cryptarithmetic Solver

This script solves cryptarithmetic puzzles where each letter represents a unique digit. The goal is to find a substitution of digits for letters such that the arithmetic equation holds true.

## Function Definition

**solve_cryptarithmetic(puzzle)**  
- **Parameters:**
  - `puzzle`: A string representing the arithmetic equation in the form "word1 word2 ... wordn", where words are strings composed of letters and spaces, e.g., "SEND MORE MONEY"

- **Returns:**
  - The digit substitution that satisfies the equation or prints a message indicating no solution was found.

## Algorithm Steps

1. **Parse Input:**  
   Split the input puzzle into words. The last word is considered the result (right side of the equation), and all previous words form the left side (left operand).

2. **Collect Unique Letters:**  
   Extract all unique letters from both sides of the equation, excluding spaces.

3. **Generate Permutations:**  
   Create permutations of digits corresponding to the number of unique letters found in the previous step. Each permutation represents a potential digit assignment for the letters.

4. **Check Validity:**  
   For each permutation:
   - Ensure that no letter (except those on the right side) starts with a zero.
   - Verify that substituting these digits into the equation results in a valid arithmetic operation.

5. **Output Result:**  
   Print the valid digit substitution when found, or indicate failure if no solution exists.

## Example Usage

To solve a puzzle like "SEND MORE MONEY", use:
```python
solve_cryptarithmetic("SEND MORE MONEY")
```

This script efficiently explores all possible digit assignments using permutations and checks for validity based on arithmetic constraints.