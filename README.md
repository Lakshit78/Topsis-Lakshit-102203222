# TOPSIS Python Package

## Overview

**TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) is a widely used multi-criteria decision analysis (MCDA) method. It helps in ranking and selecting alternatives based on a set of criteria, where each criterion may have varying importance (weight) and impact (positive or negative).

This package implements the TOPSIS method, which can be used to rank options based on input data, weights, and impacts for each criterion. The results include a ranking, the distance to the ideal best and worst solutions, and the TOPSIS score for each option.

## Features

- **Ranking**: Ranks options based on a set of criteria.
- **Flexible Inputs**: Allows users to specify weights and impacts for each criterion.
- **Ideal Solution Calculation**: Computes the distance from both the ideal best and worst solutions.
- **CSV Input and Output**: Accepts CSV files for input and generates CSV files for results.

## Installation

To install the `topsis` package, run the following command in your terminal:

```bash
pip install Topsis-Lakshit-102203222
```

## Usage

### Command-Line Usage

After installing the package, you can run the TOPSIS method from the command line using the following syntax:

```bash
python -m topsis.topsis input_data.csv "1,1,2,2,1" "+,+,-,-,-" result.csv
```

### Parameters

The command-line tool accepts the following parameters:

- **`input_data.csv`** (Required): 
  - Path to the input CSV file containing the data.
  - The first column of the CSV file should represent the options (e.g., Option1, Option2, ...).
  - The remaining columns should contain the criteria values for each option.
  
- **`"1,1,2,2,1"`** (Required): 
  - A comma-separated string representing the weights for each criterion.
  - Each number corresponds to the importance of a criterion. The higher the number, the more important the criterion is.

- **`"+,+,-,-,-"`** (Required): 
  - A comma-separated string representing the impacts for each criterion.
  - The impacts can be either:
    - `+` for positive impact: A higher value for the criterion is better.
    - `-` for negative impact: A lower value for the criterion is better.

- **`result.csv`** (Required): 
  - Path to the output CSV file where the results will be saved.
  - The output file will contain the following columns:
    - **Option**: The option name.
    - **Distance from Ideal Best**: The Euclidean distance of each option from the best possible solution.
    - **Distance from Ideal Worst**: The Euclidean distance of each option from the worst possible solution.
    - **TOPSIS Score**: A score that indicates how close each option is to the ideal solution.
    - **Rank**: The rank of each option based on its TOPSIS score (1 being the best).


## Example

### Input CSV: `input_data.csv`

```csv
Option,Criterion1,Criterion2,Criterion3,Criterion4,Criterion5
Option1,7,9,6,8,7
Option2,8,7,9,7,8
Option3,6,5,8,6,5
```

### Syntax

To use the TOPSIS method, run the following command in the terminal:

```bash
python -m topsis.topsis <input_data.csv> <weights> <impacts> <result.csv>
```

### Output CSV: `result.csv`

The output of the TOPSIS method is saved in a CSV file named `result.csv` with the following structure:

```csv
Option,Distance from Ideal Best,Distance from Ideal Worst,TOPSIS Score,Rank
Option1,2.5,5.0,0.6667,1
Option2,3.0,4.5,0.6,2
Option3,3.5,3.0,0.4615,3
```

### Understanding the Output

- **Distance from Ideal Best**: 
  - Euclidean distance of each option from the best possible solution. The ideal best solution is the one that has the maximum value in all positive impact criteria and the minimum in all negative impact criteria.

- **Distance from Ideal Worst**: 
  - Euclidean distance of each option from the worst possible solution. The ideal worst solution is the one that has the minimum value in all positive impact criteria and the maximum in all negative impact criteria.

- **TOPSIS Score**: 
  - The score that indicates how close each option is to the ideal solution. A higher score means the option is closer to the ideal solution.

- **Rank**: 
  - The ranking of each option based on its TOPSIS score (1 being the best).

## License

© 2025 Lakshit Gupta

This repository is licensed under the MIT license. See LICENSE for details.

## Additional Notes

- The package requires Python 3.6 or higher.
- Ensure the input data is clean and contains only numerical values for the criteria columns.
- The package works with CSV files where the first column contains options (e.g., Option1, Option2, etc.) and the remaining columns contain numerical values representing the criteria.

