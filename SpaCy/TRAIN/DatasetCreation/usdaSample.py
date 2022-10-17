import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
locUSDA = "./datasets/csv/food.csv"


def piechart(y):
   labels = ["one-worded","two-worded","three-worded","four-worded"]
   plt.pie(y, labels=labels)
   plt.title("Breakdown of sampled USDA branded food by word count")
   plt.savefig("figures/usdaPieDistribution.png")


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

   foodOne = cleanedData[cleanedData.str.split().apply(len) == 1] #1388
   foodtwo = cleanedData[cleanedData.str.split().apply(len) == 2] #13851
   foodThree = cleanedData[cleanedData.str.split().apply(len) == 3] #26041 
   foodFour = cleanedData[cleanedData.str.split().apply(len) == 4] #22814

   foodOne = foodOne.sample(frac=1)
   foodtwo = foodtwo.sample(n=3000)
   foodThree = foodThree.sample(n=2000)
   foodFour = foodFour.sample(n=1500)

   lists = [foodOne,foodtwo,foodThree,foodFour]

   #combine and shuffled list for final sample and reduce the bias in training
   x = pd.concat(lists).sample(frac=1)   
   
   y = np.array([len(foodOne),len(foodtwo),len(foodThree),len(foodFour)])

   piechart(y)
   return x


# if __name__ == "__main__":
#    a = dataset()

#    print(len(a))