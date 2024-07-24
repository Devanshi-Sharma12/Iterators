## ITERATORS IN PYTHON

### ITERATOR
An iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. The Python iterators object is initialized using the iter() method. 
e.g:

INPUT:
```
string = "HEY"
ch_iterator = iter(string)    #converts our iterable into iterator
 
print(next(ch_iterator))    
print(next(ch_iterator))
print(next(ch_iterator))
```

OUTPUT:
```
H
E
Y
```

### CUSTOM ITERATOR: 

Custom Iterators are used to define our own custom behaviour for objects. It uses the next() method for iteration.

1. __iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object

2. __next__(): The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object, which further uses the next() method to iterate over. This method raises a StopIteration to signal the end of the iteration.

```
class SumIterator:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.current = first
        self.end = second

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        result = self.current
        self.current += 1
        return result


my_sum_iterator = SumIterator(1, 3)
for value in my_sum_iterator:
    print(value)
```

### GENERATORS:

A Generator in Python is a function that returns an iterator using the Yield keyword.

e.g:

INPUT:
```
def simpleGeneratorFun(a,b): 
    yield a          
    yield b          
   
for value in simpleGeneratorFun(1,2):  
    print(value)
```
OUTPUT:
```
1
2
```

### USING ITERATORS WITH CSV FILE:



```
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

```









