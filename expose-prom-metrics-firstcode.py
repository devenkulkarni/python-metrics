import time
from prometheus_client import Counter, start_http_server

#print(dir(Counter)) # Printing the available functions and attributes of the Counter class to understand what we can use for creating and managing our metrics
#print(help(Counter)) # Printing the documentation for the Counter class to understand how to use it effectively for creating and managing our metrics

rows_generated = Counter(
    "rows_generated_total",
    "Total multiplication table rows generated"
)

start_http_server(8000) # Starting the Prometheus metrics server on port 8000 to expose our metrics for scraping by Prometheus
print("Prometheus metrics server is live at http://localhost:8000/metrics")

number = 5

while True: # Running an infinite loop to continuously generate multiplication tables and update the metrics, allowing us to see the metrics in real-time as they are updated
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
        rows_generated.inc()
    print("Batch finished! Keeping server alive...")    
    time.sleep(10) # Adding a delay of 10 seconds after generating each multiplication table to simulate some processing time and allow us to see the metrics being updated in real-time
