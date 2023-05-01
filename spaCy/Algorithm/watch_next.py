# building a system that will tell the user what to watch next based on the word vector similarity of the description of movies.

import numpy as np
import spacy

nlp = spacy.load('en_core_web_md')

with open('movies.txt', 'r') as f:
    descriptions = f.readlines()

def suggest_movie(description):
    # Tokenise the input description and remove stop words
    doc = nlp(description.lower())
    words1 = [token.text for token in doc if token.is_alpha and not token.is_stop]
    # Find the similarity between the input document and movies.txt
    similarity = [nlp(desc.lower()).similarity(doc) for desc in descriptions]
    # Find the index of the most similar movie
    sim_index = np.argmax(similarity)
    # Return the title of the most similar movie
    return descriptions[sim_index]

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
suggested_movie = suggest_movie(description)
print(f"We recommend: [{suggested_movie} ]for your next watch.")