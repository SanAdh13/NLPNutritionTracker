from datetime import datetime
from flask import Flask, jsonify, render_template,request
from itsdangerous import json

import SpeechToText as sp2Txt
import NER as ner
import database as db
import nutrition


app = Flask(__name__)
app.secret_key = 'dd hh' #the secret_key can be anything
app.config["UPLOAD_FOLDER"] = 'C:\\Users\\samad\\Documents\\DISSERTATION\\temp'


#landing page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save",methods=['POST'])
def record():
    f = request.files['audio_data']
    with open('temp/audio.wav','wb') as audio:
        f.save(audio)

    #pass the audio recording to speech2text to convert to text
    text = sp2Txt.speech()

    # we use the text gained on the ner model we have and return 
    displacy, dataForDB = ner.ner(text)

    db.addToFoodTable(dataForDB)

    return ("""<p>The following detected response has been added to the database</p>
    <p> Response:  """+ displacy) 

#for daily we will have it for the past 5 days , for weekly; for the past 5 weeks , for monthly past 6 months and yearly is gonna be all possible years
data = [{'option':'select option'},
        {'option':'daily'},
        {'option':'weekly'},
        {'option':'monthly'},
        {'option':'Yearly'}]
@app.route("/track")
def track():
    
    return render_template("track.html",data=data)

@app.route("/getGrouped", methods=['POST'])
def getSelection():
    selected = request.form.get('data').lower()

    if(selected != "select option"):
        if(selected == "daily"):
            vals = db.getFood(0)
        elif(selected == "weekly"):
            vals = db.getFood(1)
        elif selected == 'monthly':
            vals = db.getFood(2)    
        elif selected == "yearly":
            vals = db.getFood(3)
        
    nutrition = getNutritionInfo(vals)


    #TODO: we need to create a combined json 
    # where itll be like {"tables": vals , "nutrition": nutrition }
    #and then return that json 
    #TODO: refactor some of the Track.js so that the correct json part is being used
    # the table will use "tables" and the charts will use "nutrition"

    # https://stackoverflow.com/questions/2571702/return-multiple-values-in-jquery-ajax-call
    #as ajax can only do  (values, status, ....)  we have to pass the two things as one json obj
    # we cannot do return a, b => 
    # instead we return a jsonobj called lets say "AjoinB"

    return jsonify(vals),jsonify(nutrition)

def getNutritionInfo(data):
    nutri = nutrition(data)
    
    return nutri



@app.route('/getDates', methods=['POST'])
def getSelectionByDate():
    start = request.form.get('from')
    end = request.form.get('to')
    

    return str(start),str(end)
    #convert the string into the datetime format 
    # as our datetime has no time itll default to 00:00
    format = "%Y-%m-%d"
    startDatObj,endDatObj = datetime.strptime(start,format) , datetime.strptime(end,format)
    
    vals = db.getFoodByDateRange(startDatObj,endDatObj)
    return jsonify(vals)

if __name__ == "__main__":
    app.run(debug=True)