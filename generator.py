class Sentence:
    def sentence(sentence):
        for word in sentence.split():
            yield word
            
        
my_sentence = Sentence('My name is Devanshi Sharma')
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))