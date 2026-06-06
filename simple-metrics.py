#This python code will help understand how to generate metrics and use them in a simple way.

import time # importing built-in time module to measure execution time

# Define a list of employees
employees = ["emp1", "emp2", "emp3", "emp4"]

# Define scanned_employees as an empty variable to store the count of scanned employees
scanned_employees = 0

# Define a timer variable to measure the execution time of the scanning process
#print(dir(time)) # Printing the available functions in the time module to understand what we can use for measuring time
#print(help(time.perf_counter))
#print(help(time.process_time))

perf_start_time = time.perf_counter() # Starting the timer to measure the execution time of the scanning process
proc_start_time = time.process_time() # Starting the timer to measure the CPU time taken by the scanning process

print("Scanning Employees....")
for emp in employees:
    time.sleep(1) # Simulating the time taken to scan each employee and adding a delay of 1 second
    scanned_employees += 1 # Incrementing the count of scanned employees
    print(f"Scanned {emp}")

perf_end_time = time.perf_counter() # Ending the timer to measure the execution time of the scanning process
proc_end_time = time.process_time() # Ending the timer to measure the CPU time taken by

#print(f"Metric -> Total scanned employees: {scanned_employees}") # Printing the total count of scanned employees as a metric

perf_execution_time = perf_end_time - perf_start_time # Calculating the execution time of the scanning process
proc_execution_time = proc_end_time - proc_start_time # Calculating the CPU time taken by the scanning process

#print(f"Metric -> Execution time: {perf_execution_time} seconds") # Printing the execution time as a metric
#print(f"Metric -> CPU time: {proc_execution_time} seconds") # Printing the CPU time as a metric

metrics = {
    "scanned_employees": scanned_employees,
    "execution_time_seconds": perf_execution_time,
    "cpu_time_seconds": proc_execution_time
}

print(f"Metrics: {metrics}") # Printing all the metrics in a dictionary format for better readability and organization