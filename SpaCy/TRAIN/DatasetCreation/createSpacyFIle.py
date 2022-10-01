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
nlp = spacy.load("en_core_web_trf",disable=["tagger","parser", "attribute_ruler", "lemmatizer"])
# nlp = spacy.blank("en")


#create the .spacy file for ner annotations as required by Spacy v3
# https://spacy.io/usage/training#training-data

def toSpacy(DATA):
    db = DocBin()
    ''' we will be saving the data {foodEntities} as a .spacy format in compliance with SpaCy v3.0>'''
    for text,annotations in tqdm(DATA['annotations']):
        doc = nlp.make_doc(text)
        ents = []
        for start,end,label in annotations["entities"]:
        # for start,end,label in annotations:
            span = doc.char_span(start,end,label=label,alignment_mode="strict")
            if span is not None:
                ents.append(span)
        
        # https://stackoverflow.com/questions/67407433/using-spacy-3-0-to-convert-data-from-old-spacy-v2-format-to-the-brand-new-spacy/67459259#67459259
        try:
            doc.ents = ents
        except:
            pass    
        db.add(doc)

    return db

def saveDoc(d,TYPE):
    if TYPE == "TRAIN":
        d.to_disk("./datasets/spacyFiles/trainData.spacy")
    else:
        d.to_disk("./datasets/spacyFiles/validationData.spacy")

def loadJSON():
    ''' 
    combine the two jsons to make one spacy file
    '''
    # run the USDA entity creation files
    ent.entity()

    usda = open('./datasets/json/usdaEntity.json')
    yelp = open("./datasets/json/yelpAnnotated.json")
    
    firstData = json.load(usda)
    secondData = json.load(yelp)

    #TODO: before creating the spacy split the annotation into test train
    #maybe use the scikit test train split to do it not sure currently
 
    # length = len(foodEntity["annotations"])-10
    # print((foodEntity["annotations"][length-10:]))


    firstDB =  toSpacy(firstData) # traain
    secondDB =  toSpacy(secondData) # validation

    saveDoc(firstDB,"TRAIN")
    saveDoc(secondDB,"Validation")
   

if __name__ == "__main__":
    loadJSON()
    
    
