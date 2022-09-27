import spacy



nerModel = spacy.load("model-best")
doc = nerModel('''Mannnn who the hell is eating hotdogs at 6 in the morning 
Donald trump is threatning iraq on twitter, its kinda crazy
beans, greens, tomatoes, potatoes, rice, horse, chicken

jeff bezos decided to leave earth and live in mars i guess 
''')
ents = list(doc.ents)

for i in ents:
  print(i.label_)
  print(i.text)
  print("")
