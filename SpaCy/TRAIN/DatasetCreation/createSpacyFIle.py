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
db = DocBin()

#create the .spacy file for ner annotations as required by Spacy v3
# https://spacy.io/usage/training#training-data

def spacytoDoc(TRAIN_DATA):
    
    ''' we will be saving the data {foodEntities} as a .spacy format for ner training'''
    for text,annotations in tqdm(TRAIN_DATA['annotations']):
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

def loadJSON():
    ''' 
    combine the two jsons to make one spacy file
    '''

    # run the USDA entity creation files
    # ent.entity()

    usda = open('./datasets/usdaEntity.json')
    yelp = open("./datasets/yelpAnnotated.json")
    
    firstData = json.load(usda)
    secondData = json.load(yelp)

    spacytoDoc(firstData)
    spacytoDoc(secondData)

    # data = json.load(open("./datasets/json/ValidationAnnotations.json"))
    # spacytoDoc(data)
    db.to_disk("./datasets/spacyFiles/trainData.spacy")

if __name__ == "__main__":
    loadJSON()
    
    
