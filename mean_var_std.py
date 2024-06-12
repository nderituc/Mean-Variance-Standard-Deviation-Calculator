import streamlit as st
import numpy as np

# Function to calculate mean, variance, standard deviation, max, min, and sum
def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list into a 3x3 numpy array
    matrix = np.array(numbers).reshape(3, 3)
    
    # Calculate mean, variance, standard deviation, max, min, and sum
    mean = [list(np.mean(matrix, axis=0)), list(np.mean(matrix, axis=1)), np.mean(matrix)]
    variance = [list(np.var(matrix, axis=0)), list(np.var(matrix, axis=1)), np.var(matrix)]
    std_dev = [list(np.std(matrix, axis=0)), list(np.std(matrix, axis=1)), np.std(matrix)]
    max_val = [list(np.max(matrix, axis=0)), list(np.max(matrix, axis=1)), np.max(matrix)]
    min_val = [list(np.min(matrix, axis=0)), list(np.min(matrix, axis=1)), np.min(matrix)]
    sum_val = [list(np.sum(matrix, axis=0)), list(np.sum(matrix, axis=1)), np.sum(matrix)]
    
    # Create the dictionary with the desired format
    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
    
    return result

# Streamlit app
def main():
    st.title("Matrix Calculator")
    st.write("Enter 9 numbers to calculate various statistics of a 3x3 matrix.")
    
    # Input field for user to enter 9 numbers
    numbers = st.text_input("Enter 9 numbers separated by spaces:")
    
    # Convert input string to list of numbers
    numbers = list(map(float, numbers.split()))
    
    # Calculate statistics when user clicks the button
    if st.button("Calculate"):
        try:
            result = calculate(numbers)
            st.write("Statistics of the matrix:")
            st.write("mean:")
            st.write("Axis 1:", result['mean'][0])
            st.write("Axis 2:", result['mean'][1])
            st.write("Flattened:", result['mean'][2])
            
            st.write("variance:")
            st.write("Axis 1:", result['variance'][0])
            st.write("Axis 2:", result['variance'][1])
            st.write("Flattened:", result['variance'][2])
            
            st.write("standard deviation:")
            st.write("Axis 1:", result['standard deviation'][0])
            st.write("Axis 2:", result['standard deviation'][1])
            st.write("Flattened:", result['standard deviation'][2])
            
            st.write("max:")
            st.write("Axis 1:", result['max'][0])
            st.write("Axis 2:", result['max'][1])
            st.write("Flattened:", result['max'][2])
            
            st.write("min:")
            st.write("Axis 1:", result['min'][0])
            st.write("Axis 2:", result['min'][1])
            st.write("Flattened:", result['min'][2])
            
            st.write("sum:")
            st.write("Axis 1:", result['sum'][0])
            st.write("Axis 2:", result['sum'][1])
            st.write("Flattened:", result['sum'][2])
        except ValueError as e:
            st.error(str(e))

if __name__ == "__main__":
    main()


