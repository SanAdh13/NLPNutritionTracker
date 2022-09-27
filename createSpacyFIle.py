# this one creates the .spacy file to use for cmd training prompt after the config has been setup
# python -m spacy init fill-config base_config.cfg config.cfg
# python -m spacy train config.cfg --output ./ --paths.train TRAIN/usdaTrain.spacy --paths.dev TRAIN/usdaTrain.spacy --gpu-id 0
# 

import json
import spacy
from tqdm import tqdm
from spacy.tokens import DocBin
import createEntitySet as ent

spacy.prefer_gpu() 

#TODO: try to see if the model will create with an existing model
#TODO: if not then combine the FOOD model with existing
#TODO: look to see if i can still use the YELP set or maybe abandon it


nlp = spacy.load("en_core_web_trf")
# nlp = spacy.blank("en")
db = DocBin()

#create the .spacy file for ner annotations as required by Spacy v3
# https://spacy.io/usage/training#training-data

def makeSpacyFile(TRAIN_DATA,type):
    
    ''' we will be saving the data {foodEntities} as a .spacy format for ner training'''
    for text,annotations in tqdm(TRAIN_DATA['annotations']):
        doc = nlp.make_doc(text)
        ents = []
        for start,end,label in annotations["entities"]:
        # for start,end,label in annotations:
            span = doc.char_span(start,end,label=label,alignment_mode="strict")
            if span is None:
                pass
            else:    
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    if(type == "USDA"):        
        db.to_disk("TRAIN/usdaTrain.spacy")    
    elif type == "YELP":
        db.to_disk("TRAIN/yelpTrain.spacy")    


# def yelp():
#     yelpLoc = "SpaCy/datasets/yelpAnnotated.json"
    
#     #reads the json format annotated data
#     with open(yelpLoc,"r") as f:
#         data = json.load(f)

#     entity_name = "FOOD"
#     train_data = data['annotations']
#     train_data = [tuple(i) for i in train_data] 


#     for i in train_data:
#         if i[1]['entities'] == []:
#             i[1]['entities'] = (0,0,entity_name)
#         else:
#             i[1]['entities'][0] = tuple(i[1]['entities'][0]) 

#     makeSpacyFile(train_data,"YELP")


def usda():
    ''' we will split into test train for both sets
        then combine the resulting sets to create final testing and training

        finalTrain/Test set = yelpTrain/Test + customUSDATrain/Test 
    '''

    #run the USDA entity creation files
    ent.entity()
    # makeSpacyFile(usdaData,"USDA")

    f = open('datasets/usdaEntity.json')
    TRAIN_DATA = json.load(f)

    makeSpacyFile(TRAIN_DATA,"USDA")


if __name__ == "__main__":
    usda()
    
    



