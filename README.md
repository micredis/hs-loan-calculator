# Loan Calculator

The Loan Calculator is a command-line utility that helps users calculate either differentiated or annuity loan payments. It provides insights into monthly payments, total payments, and any overpayment.

This project is uploaded alongside the task descriptions as they were originally formulated on the Hyperskill platform.

## Features

- Calculate differentiated loan payments.
- Calculate annuity loan payments.
- Display monthly breakdown for differentiated payments.
- Intuitive command-line arguments.

## Installation

Clone the repository:

```bash
https://github.com/micredis/hs-loan-calculator.git
cd LoanCalculator
```

Ensure you have Python 3.x installed:

```bash
python --version
```

## Usage

### Command-line Arguments

- `-t` or `--type`: Type of payment. Choose between 'annuity' or 'diff'.
- `-p` or `--payment`: Monthly payment amount. Not valid for 'diff'.
- `-r` or `--principal`: Loan principal amount.
- `-n` or `--periods`: Number of payments or periods.
- `-i` or `--interest`: Annual interest rate without the % sign.

### Examples

To calculate differentiated payments:

```bash
python loan_calculator.py -t diff -r 1000000 -n 10 -i 10
```

To calculate annuity payments:

```bash
python loan_calculator.py -t annuity -r 1000000 -n 10 -i 10
```
