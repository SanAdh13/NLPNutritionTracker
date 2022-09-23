import pandas as pd
import getDatasetSample as dataset

def entity():
    templates = [ 
        " ",
        " ",
        " "
    ]

    foodEntity = []

    usda,_ = dataset.dataset()

    entityCount = usda.size -1 

    while entityCount > 1:
        entities = []

        pickedTemplate = templates[random.randint(0,len(templates)-1)]
        replacementCount = re.findall("{}",pickedTemplate)

        for x in replacementCount:
            food = usda.iloc[entitycount]

            pickedTemplace = pickedTemplate.replace(x,food,1)
            matchSpan = re.search(food,pickedTemplate).span()

            entities.append((matchSpan[0],mathcSpan[1],"FOOD"))

        foodEntity.append((sentence,{"enitites":entities}))    

    return foodEntity