number = 5 # defined the number for which we want to generate the multiplication table

rows_generated = 0 #defined a variable to count the number of rows generated in the multiplication table

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    rows_generated += 1 # Incrementing the count of rows generated for each iteration of the loop

print(f"Metric -> rows_generated={rows_generated}")