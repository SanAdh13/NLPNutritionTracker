import spacy
spacy.prefer_gpu()


# nlp = spacy.load("en_core_web_trf",disable=["tagger","parser", "attribute_ruler", "lemmatizer"])
# food_nlp = spacy.load("C:\\Users\\samad\\Documents\\DISSERTATION\\SpaCy\\model\\model-best")
# food_nlp.replace_listeners("transformer", "ner", ["model.tok2vec"])
# nlp.add_pipe(
#     "ner",
#     name="ner_food",
#     source=food_nlp,
#     after="ner",
# )
# # nlp.to_disk("../model/combined/")

nlpLoc = "SpaCy/model/combined"

def ner(text):
  nlp = spacy.load(nlpLoc)

  doc = nlp(text)
  print(doc.ents)
