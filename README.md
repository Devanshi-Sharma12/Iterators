## ITERATORS IN PYTHON


### DIFFERENCE BETWEEN ITERATOR AND INTERABLES
- **Iterable** is an object, that one can iterate over. It generates an Iterator when passed to iter() method.

- An **iterator** is an object, which is used to iterate over an iterable object using the __next__() method. Iterators have the __next__() method, which returns the next item of the object.

**Note**: Every iterator is also an iterable, but not every iterable is an iterator in Python.


### HOW TO DISTINGUISH BETWEEN AN ITERATOR AND ITERABLE?
1. Using the __next__ function:

INPUT:
```
s="Devanshi"
print(next(s))
```

OUTPUT:
```
Traceback (most recent call last):
  File "/home/1c9622166e9c268c0d67cd9ba2177142.py", line 2, in <module>
    next("Devanshi")
TypeError: 'str' object is not an iterator
```

INPUT:
```
s="HEY"
s=iter(s)
print(s)
print(next(s))
print(next(s))
print(next(s))
```

OUTPUT:
```
<str_iterator object at 0x7f822a9c3210>
H
E
Y
```

2.Using the dir and type:
INPUT:
```
s="Devanshi"
print(type(s))
iterable=iter(s)
print(type(iterable))
```
OUTPUT:
```
<class 'str'>
<class 'str_iterator'>
```


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
### Benefits of Using Iterators

1. Memory Efficiency:
Process large datasets without loading everything into memory.
2. Lazy Evaluation:
Compute values as needed, improving performance.
3. Improved Code Readability:
Simplifies code structure for iteration tasks.


### Working with csv files using iterators

Reading without an iterator:
```
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
```

OUTPUT:
```
Memory Usage without Iterators: 20480 bytes
```

Reading with an iterator
```
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

```

OUTPUT:
```
Memory Usage with Iterators: 8192 bytes
```

### Reading a csv file:

```
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
```








