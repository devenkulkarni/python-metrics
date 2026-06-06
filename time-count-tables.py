import time # importing the time module to measure the execution time of the code
import json

errors = 0 # defined a variable to count the number of errors encountered during the execution of the code
start_time = time.perf_counter() # Starting the timer to measure the execution time

# change value of 10 to ten to simulate an error and see how it affects the metrics
numbers = [2, 5, "ten"] # defined a list of numbers for which we want to generate multiplication tables

tables_generated = 0 # defined a variable to count the number of multiplication tables generated
rows_generated = 0   # defined a variable to count the total number of rows generated across all multiplication tables

for num in numbers:
    try:

        print(f"\nMultiplication Table for {num}")
        for i in range(1, 11):
            print(f"{num} x {i} = {int(num) * i}") # Attempting to convert num to an integer to perform multiplication, which will raise a ValueError if num is not a valid integer   
            rows_generated += 1
        tables_generated += 1

    except ValueError as e:

        print(f"Error processing {num}: {e}")

    errors += 1
 
    #print(f"\nMultiplication Table for {num}")

    #for i in range(1, 11):
    #    print(f"{num} x {i} = {int(num) * i}")
    #    rows_generated += 1
    
    #tables_generated += 1
    
    time.sleep(1) # Adding a delay of 1 second after generating each multiplication table to simulate some processing time

end_time = time.perf_counter() # Ending the timer to measure the execution time

execution_time = end_time - start_time # Calculating the execution time of the code

metrics = {
    "tables_generated": tables_generated,
    "rows_generated": rows_generated,
    "execution_time_seconds": execution_time,
    "errors_during_execution": errors
}

print("\nMetrics:") # Printing a header for the metrics section
print(json.dumps(metrics, indent=4)) # Printing all the metrics in a JSON format for better readability and organization

#print(f"Metrics: {metrics}") # Printing all the metrics in a dictionary format for better readability and organization

#print(f"\nMetric -> tables_generated={tables_generated}")
#print(f"Metric -> rows_generated={rows_generated}")
#print(f"Metric -> execution_time={execution_time} seconds")

# Let's derive a metric for average rows per table
#average_rows_per_table = rows_generated / tables_generated if tables_generated > 0 else 0  # Calculating the average number of rows generated per multiplication table, ensuring we don't divide by zero
#print(f"Metric -> average_rows_per_table={average_rows_per_table}")