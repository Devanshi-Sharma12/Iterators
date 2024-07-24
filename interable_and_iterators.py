class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()
        
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration  # This should raise StopIteration, not return it
        index = self.index
        self.index += 1
        return self.words[index]

my_sentence = Sentence('My name is Devanshi Sharma')
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))



