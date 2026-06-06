import time
from prometheus_client import Counter, Summary, start_http_server

# Define ALL your custom metrics
TABLES_GENERATED = Counter(
    "tables_generated_total", 
    "Total number of multiplication tables successfully completed"
)

ROWS_GENERATED = Counter(
    "rows_generated_total", 
    "Total multiplication table rows generated"
)

ERRORS_TOTAL = Counter(
    "errors_total", 
    "Total number of processing errors encountered"
)

# Similar to counter, summary is a metric type that allows us to track execution times.
CODE_EXECUTION_TIME = Summary(
    "code_execution_duration_seconds", 
    "Time spent processing a complete batch of numbers"
)

# Start the metrics server
start_http_server(8000)
print("Prometheus metrics server is live at http://localhost:8000/metrics")


numbers = [2, 5, "ten"]

# Run a Continuous Loop
while True:
    print("\n--- Starting New Processing Batch ---")
    
    # We use the summary's built-in time() context manager. 
    # It automatically starts a stopwatch right here, and stops it when this block ends.
    with CODE_EXECUTION_TIME.time():
        for num in numbers:
            try:
                print(f"\nMultiplication Table for {num}")
                for i in range(1, 11):
                    # Doing the actual math verification from your original logic
                    print(f"{num} x {i} = {int(num) * i}")
                    ROWS_GENERATED.inc()
                
                # If the inner loop finishes without throwing an error, the table succeeded!
                TABLES_GENERATED.inc()
                
            except ValueError as e:
                print(f"Error processing {num}: {e}")
                ERRORS_TOTAL.inc()
                
            # Adding 1-second delay per number simulation
            time.sleep(1)
            
    print("\nBatch finished! Keeping server alive... Next cycle starts in 10 seconds.")
    time.sleep(10)