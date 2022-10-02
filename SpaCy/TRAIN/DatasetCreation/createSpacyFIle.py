# this one creates the .spacy file to use for cmd training prompt after the config has been setup
# python -m spacy init fill-config base_config.cfg config.cfg
# python -m spacy train config.cfg --output ./ --paths.train TRAIN/usdaTrain.spacy --paths.dev TRAIN/usdaTrain.spacy --gpu-id 0
# 

import json
import spacy
from tqdm import tqdm
from spacy.tokens import DocBin
import createEntitySet as ent
import numpy as np

spacy.prefer_gpu() 
nlp = spacy.load("en_core_web_trf",disable=["tagger","parser", "attribute_ruler", "lemmatizer"])
# nlp = spacy.blank("en")


#create the .spacy file for ner annotations as required by Spacy v3
# https://spacy.io/usage/training#training-data

def toSpacy(DATA,filename):
    db = DocBin()
    ''' we will be saving the data {foodEntities} as a .spacy format in compliance with SpaCy v3.0>'''
    for text,annotations in tqdm(DATA):
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
    db.to_disk("./datasets/spacyFiles/%s.spacy"%filename)

def toTestFile(DATA):
    with open("./datasets/test.txt",'w') as file: 
        for text,_ in DATA:
            file.writelines(text + "\n")
        file.close()    

def loadJSON():
    ''' 
    combine the two jsons to make one spacy file
    '''
    # run the USDA entity creation files
    # ent.entity()

    usda = open('./datasets/json/usdaEntity.json')
    yelp = open("./datasets/json/yelpAnnotated.json")
    
    usda  = json.load(usda)
    yelp = json.load(yelp)

    '''currently we have two sets of annotated data; yelp and usda of different sizes
    
    we want to split both of these into three sets; with both sets combined 
    train.spacy,dev.spacy and test.txt [80:10:10]


    train and dev will have the entire annotated saved
    test will only have the text part, annotations removed

    '''
    np.random.shuffle(usda['annotations'])
    np.random.shuffle(yelp['annotations'])

    #getting the index of where the splits should be
    datasetSize = [len(usda['annotations']),len(yelp['annotations'])]   
    first = [int(0.8*datasetSize[0]),int(0.8*datasetSize[1])]  # [: 80%] of the set 
    second = [first[0]+int(0.1*datasetSize[0]) , first[1]+int(0.1*datasetSize[1])] #this will split the [80% : 90%] and subsequently [90%:]

    #train-dev-test split of combined usda and yelp set 
    train = usda['annotations'][:first[0]] + yelp['annotations'][:first[1]]
    dev = usda["annotations"][first[0]:second[0]] + yelp["annotations"][first[1]:second[1]] 
    test = usda['annotations'][second[0]:] + yelp['annotations'][second[1]:]   

    np.random.shuffle(train)
    np.random.shuffle(dev)
    np.random.shuffle(test)    

    #create the spacy file for test and train
    toSpacy(train,"Train")
    toSpacy(dev,"Dev")

    toTestFile(test)


if __name__ == "__main__":
    loadJSON()
    
    
