# Advanced Levenshtein Distance Calculator

## Overview

This program calculates the Levenshtein distance between two strings and provides a detailed comparison. You can customize the costs for deletion, insertion, and substitution operations.

## Features

- **Customizable Costs:** Adjust the costs of deletion, insertion, and substitution operations.
- **Object-Oriented Design:** The program is structured around a class-based system, making it modular and extendable.
- **Detailed Comparison:** Provides additional details such as string lengths, max length, and individual operation costs.

## How it Works

The Levenshtein distance is calculated using dynamic programming. The distance matrix is built based on the customizable costs, and the final Levenshtein distance is retrieved from the matrix.

### Formula

Given two strings `A` and `B`, the distance `dp[i][j]` between substrings `A[0...i]` and `B[0...j]` is computed as:

- `dp[i][j] = dp[i-1][j-1]` if `A[i] == B[j]`
- `dp[i][j] = min(dp[i-1][j] + deletion_cost, dp[i][j-1] + insertion_cost, dp[i-1][j-1] + substitution_cost)` otherwise.

### Costs:
- **Deletion Cost (Default: 1):** Removing a character from the string.
- **Insertion Cost (Default: 1):** Adding a character to the string.
- **Substitution Cost (Default: 1):** Replacing one character with another.

## Installation and Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/SudeErzurumlu/advanced-levenshtein-calculator.git
    ```

2. Install dependencies:
    ```bash
    pip install numpy
    ```

3. Run the program:
    ```bash
    python advanced_levenshtein_calculator.py
    ```

## Example

