import spacy

nlp = spacy.load('en_core_web_sm')

# Create variable gardenpathSentences with two garden path sentences.
gardenpathSentences = ['The horse raced past the barn fall.', 'When Fred eats food gets thrown.']
# Add three given garden path sentences.
gardenpathSentences.extend(['Mary gave the child a Band-Aid.','That Jill is never here hurts.', 'The cotton clothing is made of grows in Mississippi.'])

print(gardenpathSentences)
print("\n")

# Tokenise each sentence.
docs = [nlp(sentence) for sentence in gardenpathSentences]
print([[token.orth_ for token in doc] for doc in docs])
# prints named entity recognition

for doc in docs:
    ents = [(e.text, e.label_) for e in doc.ents]
    print(ents)

print("PERSON means", {spacy.explain("PERSON")})
print("GPE means", {spacy.explain("GPE")})


# What was the entity and its explanation that you looked up?
# Did the entity make sense in terms of the word associated with it?

# Answers
# I looked up NORP and GPE. NORP is an acronym of Nationalities or religious or political groups, 
# and GPE is also an acronym for Geopolitical Entity. Both make sense in temrs of associated words.