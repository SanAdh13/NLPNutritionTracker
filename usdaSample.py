import pandas as pd

locUSDA = "datasets/food.csv"

def dataset():

   def cleanup(list):
      #remove any foods with special chars
      # will also remove if theres any companies with special chars
      #eg. campbell's would be removed
      clean = list[list.str.contains("[^a-zA-Z ]")==False]
      clean = clean.apply(lambda food:food.lower())

      #split the description to find the length and remove any food with longer that 4 words
      # 1 word chips
      #2 words chicken sandwich
      #3 words bacon chicken sandwich
      #4 words peanut butter jam sandwich

      #also remove duplicates since they have no use
      clean = clean[clean.str.split().apply(len) <=4].drop_duplicates()

      return clean

   usdaDF = pd.read_csv(locUSDA)
   usdaData = usdaDF.description 


   cleanedData = cleanup(usdaData)

   foodOne = cleanedData[cleanedData.str.split().apply(len) == 1]
   foodtwo = cleanedData[cleanedData.str.split().apply(len) == 2]
   foodThree = cleanedData[cleanedData.str.split().apply(len) == 3]
   foodFour = cleanedData[cleanedData.str.split().apply(len) == 4]


   foodOne = foodOne.sample(n=500)
   foodtwo = foodtwo.sample(n=300)
   foodThree = foodThree.sample(n=150)
   foodFour = foodFour.sample(n=100)

   lists = [foodOne,foodtwo,foodThree,foodFour]

   #combine and shuffled list for final sample and reduce the bias in training
   x = pd.concat(lists).sample(frac=1)   
   
   return x
