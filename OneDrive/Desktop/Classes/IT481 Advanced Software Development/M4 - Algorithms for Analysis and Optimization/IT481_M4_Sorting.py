import pandas as pd
import time

# Load dataset from Excel file
def get_dataset(sheet_name):
    df = pd.read_excel(
        r"C:\Users\natew\OneDrive\Desktop\Classes\IT481 Advanced Software Development\M4 - Algorithms for Analysis and Optimization\IT481_M4_Dataset.xlsx",
        sheet_name=sheet_name
    )
    numbers = pd.to_numeric(df.iloc[:, 0], errors='coerce').dropna().tolist()
    return numbers

# Bubble Sort implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# measure sort time
def sort_time(sort_function, data, label):
    print(f"\nRunning {sort_function.__name__} on {label} dataset...")
    start = time.time()
    sort_function(data.copy())
    end = time.time()
    print(f"{label} dataset time: {end - start:.4f} seconds")

# Load datasets
small_data = get_dataset("Small")
medium_data = get_dataset("Medium")
large_data = get_dataset("Large")

# Display counts
print(f"Small: {len(small_data)} values")
print(f"Medium: {len(medium_data)} values")
print(f"Large: {len(large_data)} values")

# Bubble Sort & time measurements
sort_time(bubble_sort, small_data, "Small")
sort_time(bubble_sort, medium_data, "Medium")
sort_time(bubble_sort, large_data, "Large")
