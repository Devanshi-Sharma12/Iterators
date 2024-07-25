import csv
from typing import List, Iterator

class CSVIterator:
    def __init__(self, file_path: str):
            self.file = open(file_path, 'r', newline='')  
            self.iterator = iter(self.file)  

    def __iter__(self) -> Iterator[List[str]]:
        return self

    def __next__(self) -> List[str]:
        try:
            line = next(self.iterator)  
            row = line.strip().split(',') 
            return row
        except:
            StopIteration

# Usage example:
csv_iter = CSVIterator('C:\\Users\\DELL\\OneDrive\\Desktop\\experiment\\most_wickets_t20_world_cup_2024.csv')

row = next(csv_iter)
print(row)