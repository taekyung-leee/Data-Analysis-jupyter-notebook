import spacy

nlp = spacy.load("en_core_web_sm")

# Define garden path sentences
gardenpathSentences = [
    "The horse raced past the barn fell.",
    "The old man the boat.",]
extragardensentences =[
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",]
gardenpathSentences += extragardensentences

# Tokenize and perform NER on each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("=" * 50)
    print(f"Sentence: {sentence}")
    for token in doc:
        print(f"Token: {token.text}, POS: {token.pos_}, Tag: {token.tag_}, Entity: {token.ent_type_}")

# Look up and print the explanation of selected entities
print("=" * 50)
print(spacy.explain("ORG"))
print(spacy.explain("LOC"))