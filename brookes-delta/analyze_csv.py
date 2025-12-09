import pandas as pd
from delta_calculator import BrookesDeltaCalculator

# Load your data
df = pd.read_csv('my_data.csv')
categories = df['Category'].tolist()
frequencies = df['Frequency'].tolist()

# Calculate
calc = BrookesDeltaCalculator(categories, frequencies)
results = calc.calculate_delta()

print(f"Δ from CSV data: {results['delta']}")
print(f"Interpretation: {results['interpretation']}")