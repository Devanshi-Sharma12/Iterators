import argparse

class CSVIterator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(self.file_path, mode='r', newline='')
        self.header = self.file.readline().split(',')  
        self.current_line = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_line is None:
            self.current_line = self.file.readline().strip().split(',')
        
        if not self.current_line: 
            self.file.close()
            raise StopIteration
        
        fields = self.current_line
        self.current_line = None
        return fields

def main():
    parser = argparse.ArgumentParser(description='Read a CSV file and iterate over its rows.')
    parser.add_argument('file_path', type=str, help='Path to the CSV file')

    args = parser.parse_args()
    
    try:
        csv_iter = CSVIterator(args.file_path)
        print(next(csv_iter))  
        print(next(csv_iter))  
        print(next(csv_iter))  
        print(next(csv_iter))  
        
    except StopIteration:
        print("No more rows to read.")

if __name__ == "__main__":
    main()
