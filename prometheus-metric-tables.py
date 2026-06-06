from prometheus_client import Counter

#print(dir(Counter)) # Printing the available functions and attributes of the Counter class to understand what we can use for creating and managing our metrics
#print(help(Counter)) # Printing the documentation for the Counter class to understand how to use it effectively for creating and managing our metrics

rows_generated = Counter(
    "rows_generated_total",
    "Total multiplication table rows generated"
)

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    rows_generated.inc()

