numbers = [2, 5, 10] # defined a list of numbers for which we want to generate multiplication tables

tables_generated = 0 # defined a variable to count the number of multiplication tables generated
rows_generated = 0   # defined a variable to count the total number of rows generated across all multiplication tables

for num in numbers:

    print(f"\nMultiplication Table for {num}")

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
        rows_generated += 1

    tables_generated += 1

print(f"\nMetric -> tables_generated={tables_generated}")
print(f"Metric -> rows_generated={rows_generated}")

# Let's derive a metric for average rows per table
average_rows_per_table = rows_generated / tables_generated if tables_generated > 0 else 0  # Calculating the average number of rows generated per multiplication table, ensuring we don't divide by zero
print(f"Metric -> average_rows_per_table={average_rows_per_table}")