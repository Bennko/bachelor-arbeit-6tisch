import matplotlib
matplotlib.use('Agg')  # Use the Agg backend to avoid opening a window
import matplotlib.pyplot as plt
import pandas as pd
import ast
import seaborn as sns

# Seaborn settings
sns.set(style="whitegrid", font_scale=1.2)

# Maximum number of cells to consider
max_cells = 25
experiment_number = 4  # Specify the experiment number

# Path to the data file
csv_file = f'results/results_experiment{experiment_number}.csv'

# Load the CSV data into a pandas DataFrame
data = pd.read_csv(csv_file)


# Initialize list to store overlap counts
overlap_counts = [0] * max_cells

# Count overlaps for each experiment
for idx, row in data.iterrows():
    relocation_times = ast.literal_eval(row['relocation_times'])
    for i in range(max_cells):
        if relocation_times[i] > 0:
            overlap_counts[i] += 1

# Calculate probability of overlap
num_experiments = len(data)
overlap_probabilities = [count / num_experiments for count in overlap_counts]

# Create DataFrame for plotting
plot_df = pd.DataFrame({
    'Cell Number': range(1, max_cells + 1),
    'Overlap Probability': overlap_probabilities
})

# Plot with Seaborn
plt.figure(figsize=(12, 7))
sns.lineplot(x='Cell Number', y='Overlap Probability', data=plot_df, marker='o', linewidth=2)

# Customize plot
plt.xlabel('Cell Number')
plt.ylabel('Probability of Overlap')
plt.title('Probability of Overlap per Cell Across Experiments')
plt.grid(True)
plt.xticks(range(1, max_cells + 1))

# Save the plot
output_file = f'results/plots/experiment{experiment_number}_pov.png'
plt.savefig(output_file, dpi=300)
plt.close()

print(f"Plot saved as {output_file}")