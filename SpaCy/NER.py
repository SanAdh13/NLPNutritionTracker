# use this one to train the spacy with the new ner pipeline and other shit 

import json
import createEntitySet as ent
import spacy
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin

spacy.prefer_GPU()
nlp = spacy.load("en_core_web_sm")


#create the .spacy file for ner annotations as required by Spacy v3
# https://spacy.io/usage/training#training-data

def makeSpacyFile(foodEntities,type):
    
    ''' we will be saving the data {foodEntities} as a .spacy format for ner training'''
    db = DocBin()
    for text,annotations in tqdm(foodEntities):

        # print(text)
        # print(annotations)
        doc = nlp(text)
        ents = []
        for start,end,label in annotations:
            span = doc.char_span(start,end,label=label)
            ents.append(span)

    if(type == "USDA"):        
        db.to_disk("SpaCy/datasets/customTrainSpacy/usdaTrain.spacy")    
    elif type == "YELP":
        db.to_disk("SpaCy/datasets/customTrainSpacy/yelpTrain.spacy")    


def yelp():
    yelpLoc = "SpaCy/datasets/yelpAnnotated.json"
    
    #reads the json format annotated data
    with open(yelpLoc,"r") as f:
        data = json.load(f)

    entity_name = "FOOD"
    train_data = data['annotations']
    train_data = [tuple(i) for i in train_data] 


    for i in train_data:
        if i[1]['entities'] == []:
            i[1]['entities'] = (0,0,entity_name)
        else:
            i[1]['entities'][0] = tuple(i[1]['entities'][0]) 

    makeSpacyFile(train_data,"YELP")


def createTestTrain():
    ''' we will split into test train for both sets
        then combine the resulting sets to create final testing and training

        finalTrain/Test set = yelpTrain/Test + customUSDATrain/Test 
    '''

    #run the USDA entity creation files
    usdaData = ent.entity()
    makeSpacyFile(usdaData,"USDA")

    #TODO: split the two set into test trains set and combine to have one final train and test




############ this will start the training for the ner

#TODO: create the new ner pipeline
# train the new pipeline with the created .spacy files
#test this new model with test data and extract the relevant items

def NERStart():
    return 0



