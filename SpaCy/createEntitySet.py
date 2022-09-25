
import random
import re
import usdaSample as dataset

''' we need to create the entity set for training the ner'''

'''for the yelp dataset as we dont have to create one but instead use an internet annotation tool '''

'''
    we will use the usda food items sampled in getDatasetSample.py to create the entities 

    the entities should be the format

    "text", [entities:{startingIndex,endingIndex,"FOOD"},{startingIndex,endingIndex,"FOOD"}] 
    
    or 

    "text", [{startingIndex,endingIndex,"FOOD"},{startingIndex,endingIndex,"FOOD"}]

    i=0 will be the text, i=1 the entities 
'''

def entity():
    #TODO: add more values to the template
    templates = [ 
        " Today i ate {} ",
        "For lunch i had {} , {} and {} ",
        " I decided to have a portion of {} ,and some {} "
    ]

    foodEntity = []

    usda = dataset.dataset()

    entityCount = usda.size -1 

    while entityCount > 1:
        entities = []

        pickedTemplate = templates[random.randint(0,len(templates)-1)]
        replacementCount = re.findall("{}",pickedTemplate)


        for x in replacementCount:
            food = usda.iloc[entityCount]

            pickedTemplate = pickedTemplate.replace(x,food,1)
            matchSpan = re.search(food,pickedTemplate).span()

            #this will add the "(starting index, endingIndex,"FOOD") to list
            entities.append((matchSpan[0],matchSpan[1],"FOOD"))
            entityCount-= 1 

        # foodEntity.append((pickedTemplate,{"entities":entities}))  
        foodEntity.append((pickedTemplate,entities))
    return foodEntity




