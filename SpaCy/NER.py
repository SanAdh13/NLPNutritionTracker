# use this one to train the spacy with the new ner pipeline and other shit 

import createEntitySet as ent
import pandas as pd
import spacy

spacy.prefer_GPU()
spacy.load()

annotatedLoc = "SpaCy/datasets/annotated/"

def createTestTrain():
    ''' we will split into test train for both sets
        then combine the resulting sets to create final testing and training

        finalTrain/Test set = yelpTrain/Test + customUSDATrain/Test 
    '''

    #TODO: split the two annotated sets into train test using sklearn? or spacy

