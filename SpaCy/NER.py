# use this one to train the spacy with the new ner pipeline and other shit 

import json
import createEntitySet as ent
import spacy
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_trf")


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
        # for start,end,label in annotations["entities"]:
        for start,end,label in annotations:
            span = doc.char_span(start,end,label=label)
            ents.append(span)


    #TODO: the spacy file is not working, fix this
    #possible save the sampled as json and 
    # then load it and to save as .doc
    ''' AssertionError: [E923] It looks like there is no proper 
    sample data to initialize the Model of component 'ner'.
     To check your input data paths and annotation, 
     run: python -m spacy debug data config.cfg and
      include the same config override values you would specify
       for the 'spacy train' command '''

    #maybe save in the format 
    '''
    {
        classes":["FOOD"],"annotations":[["text",{"entities":[[start, end,"FOOD"]]}],
        ["text",{"entities":[[start, end,"FOOD"]]}]]
    }
    instead of current format which is 
    "text",{entities:[[s,e,"FOOD"]]}
    '''
    if(type == "USDA"):        
        db.to_disk("SpaCy/usdaTrain.spacy")    
    elif type == "YELP":
        db.to_disk("SpaCy/yelpTrain.spacy")    


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


def usda():
    ''' we will split into test train for both sets
        then combine the resulting sets to create final testing and training

        finalTrain/Test set = yelpTrain/Test + customUSDATrain/Test 
    '''

    #run the USDA entity creation files
    usdaData = ent.entity()
    makeSpacyFile(usdaData,"USDA")






############ this will start the training for the ner

#TODO: load ner pipeline
# get .spacey files for the two
# generate config file to train 
# load the saved model
# use speech recog to get the unseen data to test model prediction 
# render the result

def NERStart():
  usda()
#   yelp()


#   nerModel = spacy.load(
#     "SpaCy/model/model-last"
#   )


if __name__ == "__main__":
    NERStart()
    
    



