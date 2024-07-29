import csv
import psutil
import os

def read_csv_without_iterators(file_path):
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss 

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)  
        for row in data:
            print(row) 

    mem_after = process.memory_info().rss 
    print(f"Memory Usage without Iterators: {mem_after - mem_before} bytes")

# Call the function
read_csv_without_iterators('C:\\Users\\DELL\\OneDrive\\Desktop\\experiment\\most_wickets_t20_world_cup_2024.csv')