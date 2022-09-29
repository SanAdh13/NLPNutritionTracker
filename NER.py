import spacy
spacy.prefer_gpu()

# vocab = ["FOOD"]
nlp = spacy.load("en_core_web_sm",disable=["tagger","parser", "attribute_ruler", "lemmatizer"])

# nlp = spacy.load("en_core_web_sm")
print(nlp.pipe_names)

food_nlp = spacy.load("SpaCy\FirstModel\model-best")
print(food_nlp.pipe_names)

food_nlp.replace_listeners("tok2vec", "ner", ["model.tok2vec"])
nlp.add_pipe('ner',source=food_nlp,name="food_ner",before="ner")
# nlp.to_disk("mainModel")

doc = nlp('''Mannnn who the hell is eating hotdogs at 6 in the morning. 
Donald Trump is threatning iraq on twitter, its kinda crazy
beans, greens, tomatoes, potatoes, rice, horse, chicken.
jeff bezos decided to leave earth and live in mars i guess. 
I need 42 mules, 12 acres and everything inbetween.
''')

for ent in doc.ents:
  print(ent.text,ent.label_)
