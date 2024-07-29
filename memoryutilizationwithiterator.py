import csv
import psutil
import os

def read_csv_with_iterators(file_path):
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info() 

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:  
            print(row)  

    mem_after = process.memory_info()
    print(f"Memory Usage with Iterators: {mem_after - mem_before} bytes")


read_csv_with_iterators('C:\\Users\\DELL\\OneDrive\\Desktop\\experiment\\most_wickets_t20_world_cup_2024.csv')
