import spacy
from spacy import displacy
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

def createList(doc):
    i = 0 
    lenEnts = len(doc.ents)
    while i < lenEnts:
        currEnt = doc.ents[i] # the current ent
        try: 
            nextEnt = doc.ents[i+1] # the next ent in order to check
        except: 
            pass

        print(currEnt.label_, nextEnt.label_)

        if(currEnt.label_ == "CARDINAL") and nextEnt.label_ == "FOOD":
            i+=1
            arr.append([nextEnt.text,currEnt._.numerize()])
        else:
            if (currEnt.label_ == "FOOD"): 
                arr.append([currEnt.text,1])
        i+=1

'''
Explanation: 
displacyEnts returns the displacy format of the input text so it can be visualised in the modal

arr is the 2d list that should be useful for the database
  itll only look at cardinal and food
   and the format will be [[food,n],[food,n]] where food is the food item and n is the quantity
'''

def ner(text):
  nlp = spacy.load(nlpLoc)

  doc = nlp(text)
  displacyEnts = displacy.render(doc,style="ent")

  arr=[]
  
  #if the ent list is larger than 1 then we can do the 
  if len(doc.ents) == 1 and doc.ents[0].label_ == 'FOOD':
      arr.append([doc.ents[0].text , 1])
  else:
      createList(doc)


  print(arr)
  print(doc.ents)

  return displacyEnts, arr
