# use this one to train the spacy with the new ner pipeline and other shit 

import createEntitySet as ent
import pandas as pd
import spacy

spacy.prefer_GPU()
spacy.load()

