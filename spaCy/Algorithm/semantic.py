import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# similairty between same species/category is higher than others. 


my_example = nlp('bird banana airplane pizza')

for token1 in my_example:
    for token2 in my_example:
        print(token1.text, token2.text, token1.similarity(token2))

# in my example, similarity between bird and airplane is higher than others as both objects can fly. 
# also, the similarty between banana and pizza is high as both of them are edible. 

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)


# Difference between 'sm' and 'md' is that 'md' compares the similiary between given words, 
# while 'sm' compares the tagger, parser and NER of the given words. 