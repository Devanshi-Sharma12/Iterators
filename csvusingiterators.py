class CSVIterator:
    def __init__(self, file_path):
        self.file = open(file_path, 'r')
        self.line = self.file.readline()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.line:
            raise StopIteration
        row = self.line.split(',')
        self.line = self.file.readline()
        return row


csv_iter = CSVIterator('C:\\Users\\DELL\\OneDrive\\Desktop\\experiment\\most_wickets_t20_world_cup_2024.csv')

print(next(csv_iter)) #prints the consecutive row

