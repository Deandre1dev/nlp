# Import the module spacy. 
import spacy 

# Load spacy language model.
nlp = spacy.load('en_core_web_sm')

# list of all the gardenpath sentences.
gardenpathSentences = ["The complex houses married and single soldiers and their families.", "The horse raced past the barn fell.", " Mary gave the child a Band-Aid.", "That Jill is never here hurts.", " The cotton clothing is made of grows in Mississippi."]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([token.orth_ for token in doc]) # Tokenise each sentence.
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_) # Print every entity in each sentence.
    print(spacy.explain("GPE"))
    print(spacy.explain("PERSON"))


# GPE 
# The entity is GPE and the explanation i looked up is "a geographical region defined by political or social groups." - from the output[Countries, cities, states]
# It does make sense in terms of the word associated with it.

# PERSON
# The entity is PERSON and the explanation i looked up is "a human being or individual." - from the output[People, including fictional]
# # It does make sense in terms of the word associated with it.