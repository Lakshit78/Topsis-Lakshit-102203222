import sys
import pandas as pd
import numpy as np

def validate_inputs(input_file, weights, impacts, result_file):
    # Check if the input file exists
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Check if the file has at least 3 columns
    if data.shape[1] < 3:
        print("Error: The input file must have at least 3 columns.")
        sys.exit(1)

    # Ensure all columns from the 2nd to the last contain numeric values only
    # Ensure all columns from the 2nd to the last contain numeric values only
    if not data.iloc[:, 1:].apply(lambda col: pd.api.types.is_numeric_dtype(col)).all():
        print("Error: Columns from the 2nd to the last must contain numeric values only.")
        sys.exit(1)


    # Check if weights and impacts are separated by commas
    weights_list = weights.split(",")
    impacts_list = impacts.split(",")

    # Ensure the number of weights, impacts, and columns (2nd to last) are the same
    if len(weights_list) != len(impacts_list) or len(weights_list) != (data.shape[1] - 1):
        print("Error: The number of weights, impacts, and columns (2nd to last) must be the same.")
        sys.exit(1)

    # Ensure weights are numeric
    try:
        weights_list = [float(w) for w in weights_list]
    except ValueError:
        print("Error: Weights must be numeric values separated by commas.")
        sys.exit(1)

    # Ensure impacts are either '+' or '-'
    if not all(impact in ["+", "-"] for impact in impacts_list):
        print("Error: Impacts must be either '+' or '-' separated by commas.")
        sys.exit(1)

    print("All inputs are valid!")
    return data, weights_list, impacts_list



def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    # Collect command-line arguments
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]

    # Validate inputs
    data, weights_list, impacts_list = validate_inputs(input_file, weights, impacts, result_file)

    #Normalization of data
    numeric_data = data.iloc[:, 1:]
    normalized_matrix = numeric_data.apply(lambda col: col / np.sqrt((col**2).sum()), axis=0)

    #Multiplying weights
    weighted_normalized_matrix = normalized_matrix * weights_list

    
    df_normalized = data.copy()
    df_normalized.iloc[:, 1:] = weighted_normalized_matrix

    #Calculate Ideal Best and Ideal Worst
    ideal_best = []
    ideal_worst = []

    for i, impact in enumerate(impacts_list):
        column = data.iloc[:, i + 1]  
        if impact == "+":
            ideal_best.append(column.max())  # Max for +
            ideal_worst.append(column.min())  # Min for +
        else:
            ideal_best.append(column.min())  # Min for -
            ideal_worst.append(column.max())  # Max for -

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Calculate Euclidean Distances
    weighted_values = df_normalized.iloc[:, 1:].values  

    euclidean_best = np.sqrt(((weighted_values - ideal_best) ** 2).sum(axis=1))

    euclidean_worst = np.sqrt(((weighted_values - ideal_worst) ** 2).sum(axis=1))

    # Calculate TOPSIS Score
    topsis_score = euclidean_worst / (euclidean_best + euclidean_worst)

    df_normalized["Distance from Ideal Best"] = euclidean_best
    df_normalized["Distance from Ideal Worst"] = euclidean_worst
    df_normalized["TOPSIS Score"] = topsis_score
    df_normalized["Rank"] = pd.Series(topsis_score).rank(ascending=False).astype(int)


    try:
        df_normalized.to_csv(result_file, index=False)
        print(f"Results saved to '{result_file}'.")
    except Exception as e:
        print(f"Error saving result file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
