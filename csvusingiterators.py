import csv

class CSVIterator:
    def __init__(self, file_path):
        self.file = open(file_path, 'r')
        self.csv_reader = csv.reader(self.file)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.csv_reader)
        except:
            StopIteration

csv_iter = CSVIterator('C:\\Users\\DELL\\OneDrive\\Desktop\\experiment\\most_wickets_t20_world_cup_2024.csv')

for row in csv_iter:
    print(row) 
