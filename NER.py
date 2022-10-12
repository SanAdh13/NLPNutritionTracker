import spacy
from spacy import displacy
import numerizer

spacy.prefer_gpu()

nlpLoc = "SpaCy/model/combined"

def createList(doc,arr):
    i = 0 
    lenEnts = len(doc.ents)
    while i < lenEnts:
        currEnt = doc.ents[i] # the current ent
        try: 
            nextEnt = doc.ents[i+1] # the next ent in order to check
            if(currEnt.label_ == "CARDINAL" or currEnt.label_ == "QUANTITY") and nextEnt.label_ == "FOOD":
                i+=1
                #if the number need to be changed from word to numbers, numerize will do it. otherwise itll save as its current state
                arr.append([nextEnt.text,currEnt._.numerize()])
            else:   
                #either the label is not cardinal/quantity or not food, if it just cardinal/quantity with no food item next we disregard it
                if (currEnt.label_ == "FOOD"):  
                    arr.append([currEnt.text,1])
        except: 
            if (currEnt.label_ == "FOOD"): 
                arr.append([currEnt.text,1])
            pass
        i+=1
    return arr
'''
Explanation: 
displacyEnts returns the displacy format of the input text so it can be visualised in the modal

arr is the 2d list that should be useful for the database
  itll only look at cardinal and food
   and the format will be [[food,n],[food,n]] where food is the food item and n is the quantity
'''
 
# need to look at both weights and quantity but the format should still be same 
# in the speech its expected the speech is like " I ate QUANTITY/CARDINAL of FOOD  " 
# like previously said if the speech is not amount followed by the food this will not pick up the amount
# so in the for loop we just check if its either quantity or cardinal instead of just cardinal 

def ner(text):
  nlp = spacy.load(nlpLoc)

  doc = nlp(text)
  displacyEnts = displacy.render(doc,style="ent")

  arr=[]
  
  #if the ent list only has one object and its label is food then just add that to db
  if len(doc.ents) == 1 and doc.ents[0].label_ == 'FOOD':
      arr.append([doc.ents[0].text , 1])
  else:
      arr = createList(doc,arr)

#   print(arr)
#   print(doc.ents)

  return displacyEnts, arr
